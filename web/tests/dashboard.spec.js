import {test,expect} from '@playwright/test';
import fs from 'node:fs/promises';
test.beforeEach(async({page})=>{await page.goto('/');await expect(page.getByRole('heading',{name:'Vector search trade-offs'})).toBeVisible()});
test('measured report, constraints and detail evidence',async({page})=>{
 await expect(page.getByText('Measured performance · synthetic vectors')).toBeVisible();
 await expect(page.locator('.recommendation strong')).toHaveText('HNSW ef16');
 await page.locator('#memory').selectOption('0.3');
 await expect(page.locator('.recommendation strong')).toHaveText('Relax a constraint');
 await page.getByRole('button',{name:'HNSW ef64',exact:true}).click();await expect(page.getByRole('dialog')).toContainText('98.9%');await page.keyboard.press('Escape');await expect(page.getByRole('dialog')).not.toBeVisible();
});
test('SQLite filtering and injection-safe query ID search',async({page})=>{
 await page.getByRole('button',{name:'Query explorer',exact:true}).click();await expect(page.getByRole('heading',{name:'50,000 matching mock queries'})).toBeVisible();
 await page.getByLabel('Engine',{exact:true}).selectOption('pgvector');await expect(page.getByRole('heading',{name:'16,667 matching mock queries'})).toBeVisible();
 await page.getByLabel('Query ID').fill("' OR 1=1 --");await expect(page.getByText('No matching queries. Try another ID.')).toBeVisible();
});
test('pagination and filtered CSV export',async({page})=>{
 await page.getByRole('button',{name:'Query explorer',exact:true}).click();await page.getByRole('button',{name:'Next',exact:true}).click();await expect(page.getByText('Page 2 of 3334')).toBeVisible();
 await page.getByLabel('Query ID').fill('50000');
 const pending=page.waitForEvent('download');await page.getByRole('button',{name:'Export filtered CSV'}).click();const d=await pending;const text=await fs.readFile(await d.path(),'utf8');expect(text).toContain('50000,pgvector,HNSW');expect(text.trim().split('\n')).toHaveLength(2);
});
test('database export is SQLite',async({page})=>{
 await page.getByRole('button',{name:'Query explorer',exact:true}).click();const pending=page.waitForEvent('download');await page.getByRole('button',{name:'Export SQLite'}).click();const d=await pending;const bytes=await fs.readFile(await d.path());expect(bytes.subarray(0,15).toString()).toBe('SQLite format 3');
});
test('methodology discloses limitations and pending work',async({page})=>{
 await page.getByRole('button',{name:'Methodology',exact:true}).click();await expect(page.getByText('Real text embeddings, isolated memory measurements, database engine comparisons, sharding, Spark and GPU experiments remain pending.')).toBeVisible();
});
test('responsive layouts and reduced motion',async({page})=>{
 for(const width of [1440,1024,768,390,320]){await page.setViewportSize({width,height:1000});await expect(page.getByRole('heading',{name:'Vector search trade-offs'})).toBeVisible();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);await page.screenshot({path:`../artifacts/screenshots/dashboard-${width}.png`,fullPage:true});}
 await page.emulateMedia({reducedMotion:'reduce'});expect(await page.locator('nav button').first().evaluate(el=>getComputedStyle(el).transitionDuration)).toBe('0s');
});
