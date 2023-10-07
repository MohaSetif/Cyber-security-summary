<script lang="ts">
	import { sections } from '$lib/index';
	import { page } from '$app/stores';
	import Reveal from '$lib/reveal.svelte';
	$: neigbors = findNeigbors($page.url.pathname);
	function findNeigbors(pathname: string) {
		let location = pathname.split('/').at(-1)!;
		const decodedString = decodeURIComponent(location);
		const currentIndex = sections.indexOf(decodedString);
		return [sections[currentIndex - 1], sections[currentIndex + 1]];
	}
</script>

<div class="section">
	<div>
		<a href="/">Emotet</a>
		<div>
			{#if neigbors[0]}
				<a href="/sections/{neigbors[0]}">Previous</a>
			{/if}
			{#if neigbors[1]}
				<a href="/sections/{neigbors[1]}">Next</a>
			{/if}
		</div>
	</div>
	{#key $page.url.pathname}
		<Reveal mdFile={$page.url.pathname.split('/').at(-1)} />
	{/key}
</div>

<style>
	.section {
		width: 100vw;
		height: 100vh;
		display: flex;
		flex-direction: column;
	}
	.section div:first-child {
		width: 100%;
		height: 80px;
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-inline: 5%;
	}

	.section > div > a {
		font-size: var(--h3);
	}
	.section > div > div > a {
		font-size: var(--h4);
		margin-left: 10px;
	}
	.section > div > div > a:hover {
		background-color: var(--primary100);
		color: var(--primary800);
		padding-inline: 6px;
		padding-block: 4px;
		border-radius: 8px;
	}
</style>
