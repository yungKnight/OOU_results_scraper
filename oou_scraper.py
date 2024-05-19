import pytest
from playwright.async_api import async_playwright
import asyncio
import os
import re
import json
import scrapy
from scrapy.http import HtmlResponse

@pytest.mark.asyncio
async def test_result_extraction():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        folder = 'results'
        os.makedirs(folder, exist_ok=True)

        page = await browser.new_page()
        url = 'https://stdportal.oouagoiwoye.edu.ng/index.php'
        await page.goto(url, timeout=0)

        matric = input("Enter matric number: ")
        pword = input("Enter password: ")

        await page.wait_for_selector('input#jamb')
        await page.wait_for_selector('input#sname')
        await page.wait_for_selector('button.btn')

        await page.fill("input#jamb", matric)
        await page.fill("input#sname", pword)
        await page.click('button.btn')

        print('navigating to dashboard')
        await page.goto('https://stdportal.oouagoiwoye.edu.ng/dashboard.php')
        print('navigated to dashboard')

        await page.wait_for_selector('tbody')

        personal = await page.query_selector_all('h4 span strong')
        if personal:
            name_element = personal[0]
            status_element = personal[1]

            name = await name_element.inner_text()
            status = await status_element.inner_text()
            
            pattern = re.compile(r'^([A-Z]+),\s*([A-Z])[a-z]*(?:\s+([A-Z]))?[a-z]*')

            match = re.match(pattern, name)
            if match:
                last_name = match.group(1)
                first_name_initial = match.group(2)
                middle_name_initial = match.group(3)
                formatted_name = f"{last_name} {first_name_initial}.{middle_name_initial}"
            else:
                formatted_name = name

            formatted_status = status.capitalize()

            print(formatted_name, formatted_status)

        await page.wait_for_selector('div.modal-content')
        remove_overlay = await page.wait_for_selector('div.modal-header span.close')
        await remove_overlay.click()

        button = await page.query_selector('a[href="results.php"]')
        await button.click()
        print('clicked result hyperlink successfully')

        await page.wait_for_selector('div.col-xs-12.col-sm-6')
        print('results now present on page')

        your_result = []

        html_content = await page.content()

        response = HtmlResponse(url=page.url, body=html_content.encode(), encoding='utf-8')

        results = response.css('div.form-group')[1:-2]

        for result in results:
            reflect = {
                'Session': result.css('div.col-sm-2::text').get().strip(),
                'Semester': result.css('div.col-sm-2:nth-child(2)::text').get().strip(),
                'Course': result.css('div.col-sm-1::text').get().strip(),
                'Grade': result.css('div.col-sm-1:nth-child(6)::text').get().strip()
            }
            your_result.append(reflect)

        file_name = f'result_{formatted_name}.json'
        file_path = os.path.join(folder, file_name)

        with open(file_path, 'w') as json_file:
            json.dump(your_result, json_file, indent=6)
            print(f'Items extracted and saved')

        await browser.close()