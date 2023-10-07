<script lang="ts">
	import { sections } from '$lib/index';
	import './../app.css';
</script>

<div class="main">
	<h1>Emotet presentation</h1>
	<div class="links">
		{#each sections as section}
			<a href="/sections/{section}">{section}</a>
		{/each}
	</div>
</div>

<style>
	.main {
		width: 100vw;
		height: 100vh;
		display: flex;
		justify-content: space-evenly;
		align-items: center;
	}
	.main h1 {
		width: 25%;
	}
	.links {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}
	.links a {
		background-color: var(--primary100);
		color: var(--primary800);
		padding-inline: 6px;
		padding-block: 4px;
		border-radius: 8px;
	}
	.links a:hover {
		background-color: var(--primary400);
	}
</style>
