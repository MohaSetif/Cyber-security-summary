import type { Load } from '@sveltejs/kit';
import fs from 'fs';
import path from 'path';

export const load: Load = async ({ params }) => {
	const section = decodeURIComponent(params.name!);
	const sectionPath = path.join('static', 'sections', section + '.md');
	const data = fs.readFileSync(sectionPath);
	return {
		md: data.toString()
	};
};
