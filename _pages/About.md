---
title: "소개페이지"
permalink: /about/
layout: single
author_profile: True
---

<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>How에서 Why로 문제를 접근해 나아가는 조성곤입니다.</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
}

.simple-table-header {
	background: rgb(247, 246, 243);
	color: black;
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-opaquegray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="4ca65e87-4cc9-450f-8ea7-9cfdefe6163f" class="page sans"><header><img class="page-cover-image" src="https://www.notion.so/images/page-cover/gradients_11.jpg" style="object-position:center 40%"/><div class="page-header-icon page-header-icon-with-cover"><img class="icon" src="How%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5%20Why%E1%84%85%E1%85%A9%20%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A6%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%8C%E1%85%A5%E1%86%B8%E1%84%80%E1%85%B3%E1%86%AB%E1%84%92%E1%85%A2%20%E1%84%82%E1%85%A1%E1%84%8B%E1%85%A1%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%8C%E1%85%A9%E1%84%89%E1%85%A5%E1%86%BC%E1%84%80%E1%85%A9%E1%86%AB%204ca65e874cc9450f8ea79cfdefe6163f/%E1%84%91%E1%85%B3%E1%84%89%E1%85%A1.jpeg"/></div><h1 class="page-title">How에서 Why로 문제를 접근해 나아가는 조성곤입니다.</h1></header><div class="page-body"><hr id="00f9ab8c-f50b-458a-8338-bd13377f0318"/><h3 id="2a3023b1-5e78-40ec-bd8c-8ffdd927476c" class=""><mark class="highlight-orange">Contact.</mark></h3><p id="aad0563a-9f54-4c48-a4fe-644019aa3ab6" class=""><strong>Email</strong>. jmsmg1@me.com</p><p id="29853c13-309b-4003-8b32-2c5c57ca6410" class=""><strong>Phone</strong>. 010-8634-4491</p><h3 id="6222723a-7976-4c74-96da-f075cffa9094" class=""><mark class="highlight-orange">Channel.</mark></h3><p id="f2a44bfb-36da-45a1-91c2-1bd2895c717e" class=""><strong>Blog. </strong><a href="https://jmsmg.github.io">https://jmsmg.github.io/</a></p><p id="e32f05a4-9409-4b0b-8205-83f5565dd289" class=""><strong>instagram</strong>. <a href="https://www.instagram.com/gon__926/">https://www.instagram.com/gon__926</a></p><p id="01d441c3-a745-44b5-8dbc-68fb4a783806" class=""><strong>GitHub</strong>. <a href="https://github.com/jmsmg">https://github.com/jmsmg</a></p><hr id="092ea8ac-6fa1-4a78-a749-2aa5c406981d"/><h1 id="5a9f7c26-ff49-45be-ba36-1f2ea8df8585" class="block-color-orange"><mark class="highlight-orange">Introduce.</mark></h1><ul id="8e3882db-0211-4ba2-bb1d-e91492a61565" class="bulleted-list"><li style="list-style-type:disc"><mark class="highlight-blue"><strong>꾸준함</strong></mark>을 믿고 TIL을 실천하고 있습니다.</li></ul><ul id="a9143707-d762-4d44-a853-d6d4287ceeb0" class="bulleted-list"><li style="list-style-type:disc">Data에 대한 <mark class="highlight-blue"><strong>다양한 관점</strong></mark>을 모두 수용하고, 저와 다른 관점을 알아가는 것에 흥미를 느낍니다.</li></ul><ul id="92bb087f-12f5-4f82-b1a4-55723bd3761f" class="bulleted-list"><li style="list-style-type:disc"><mark class="highlight-blue"><strong>음악</strong></mark>을 좋아하고, 새로운 친구들을 사귀는 것에서 행복을 느낍니다.</li></ul><hr id="0d828340-24bf-494e-92fb-62b2889f87fb"/><h1 id="952e91a8-2cc0-48c7-82ff-6e6a1d408261" class=""><mark class="highlight-orange">Project.</mark></h1><h3 id="135e448c-03e7-4fd9-89ea-8c71e4623a29" class=""><a href="https://dacon.io/myprofile/430701/home">HAICon2021 산업제어시스템 보안위협 탐지 AI 경진대회</a></h3><p id="b3673bea-45f4-4762-b329-1e2e933a020e" class=""><strong>(2021.08.02~2021.10.22)</strong></p><ul id="6d676542-282a-42d1-8404-3c69a416e45c" class="bulleted-list"><li style="list-style-type:disc">상위 38%</li></ul><ul id="2eed0243-aec1-4926-b783-0ff13eb47860" class="bulleted-list"><li style="list-style-type:disc">🖐 Main role : 전처리, HPO, 이전 수상작 분석 </li></ul><p id="aa2d3ed0-a39f-4aa5-947b-c5eb6cec0db3" class=""># Exponential Smoothing  # RNN # GRU # HPO # Deep Learning # Python # PyTorch</p><hr id="ec82c414-51bb-4f1b-ab53-45e55d782a60"/><h3 id="6962688c-777c-4149-81f6-8c901f13658f" class=""><a href="https://github.com/jmsmg/TIL/tree/main/프로젝트/Final_Musinsa_Style_review">M사 스타일리뷰 적립금 지급 대상판정 system개발</a></h3><p id="f405d28a-0ab0-4be3-b27c-7861551937f7" class=""><strong>(2021.08.03~2021.08.13)</strong></p><ul id="c0982392-7eb6-421c-bb3c-8a6c8d1b8632" class="bulleted-list"><li style="list-style-type:disc"><mark class="highlight-blue"><strong>95.51% Accuracy</strong></mark></li></ul><ul id="17c3b64c-d800-4231-bd88-ed0011a2253c" class="bulleted-list"><li style="list-style-type:disc">적립금 지급 대상 Image를 분류하고 학습시킨 모델을 바탕으로 판정하는 웹 페이지 개발</li></ul><ul id="c3b6e8e4-4254-4b1b-9e1f-ec3d9af5c567" class="bulleted-list"><li style="list-style-type:disc">🖐 Main role : Web Scraping, Web개발 일부, AWS(EC2)</li></ul><p id="d6e23132-4871-4b3c-ab99-378e756f3ce3" class=""># Data Augmentation # Image Data # CNN # HPO # Transition Learning # Deep Learning</p><p id="8c3d9263-1b28-4dd2-8320-bb810ce3a687" class=""># Python # Django # Tensorflow # Selenium # Keras-tuner # Scraping</p><hr id="ea23229b-0aa1-411b-bc3d-4d9779c8e694"/><h3 id="ec2f63c0-6e2f-4792-85c6-a42a99900ae8" class=""><a href="https://github.com/jmsmg/TIL/tree/main/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/Semi3_%EC%8B%A0%EC%9A%A9%EC%B9%B4%EB%93%9C%20%EA%B3%A0%EA%B0%9D%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D%EC%9D%84%20%ED%86%B5%ED%95%9C%20%5B%EC%9C%A0%EC%A7%80%20_%20%EC%9D%B4%ED%83%88%5D%20%EA%B3%A0%EA%B0%9D%20%EC%98%88%EC%B8%A1">신용카드 고객 데이터 분석을 통한 [유지, 이탈] 고객 예측</a></h3><p id="b49178f2-8bd6-46ad-ad72-3563189e110a" class=""><strong>(2021.07.19~2021.07.28)</strong></p><ul id="c3e57385-e8e2-4d44-a90f-c56c31361bb5" class="bulleted-list"><li style="list-style-type:disc">Kaggle에 신용카드 데이터 분석을 통한 유지, 이탈 분석</li></ul><ul id="52d20bde-058f-4215-9cf2-3da48942a4aa" class="bulleted-list"><li style="list-style-type:disc">🖐 Main role : Pre-processing, Model 적용 일부</li></ul><p id="3812e812-9459-4f20-ba2e-26e523a7fe9d" class=""># MachineLearning # GridSearch # HPO # Onehot Encoder # Pycaret # Keras-tuner</p><hr id="fd53c9d0-cd3e-421e-bdd6-a35fee30d66e"/><h3 id="cd97be98-63aa-4867-8290-a7eb4b1d0912" class=""><a href="https://github.com/jmsmg/TIL/tree/main/프로젝트/Semi1_청산가치와%20주가변동의%20관계에%20대해서">청산가치를 통한 주식 종가 예측</a></h3><p id="91cc1d50-9ae4-414c-aa84-660f6d9abad8" class=""><strong>(2021.06.17~2021.06.23)</strong></p><ul id="c9e059ba-2c8f-4058-a178-b8c7fb01a13a" class="bulleted-list"><li style="list-style-type:disc">워런버핏의 투자 지표중 하나인 청산가치 및 이동평균선 기반 주식 종가 예측 서비스</li></ul><ul id="294a5154-925b-4731-b7c4-a4f1d3c36bc2" class="bulleted-list"><li style="list-style-type:disc">🖐 Main role : Web Scraping, API 활용</li></ul><p id="11727c62-6351-4877-a0ba-31f9cf9ec478" class=""># Wordcloud # Scraping # Regression # API</p><p id="409a55bc-0bfe-45b8-b6c6-1c67f73ef5f5" class=""># Python # SckitLearn # BeautifulSoup # DART</p><hr id="9c576b25-531c-4c76-84dc-73abe6724b5a"/><h1 id="c53ee5bb-bf6f-4735-b48e-8c8be91ea7cd" class=""><mark class="highlight-orange">Work experience.</mark></h1><h3 id="f7694080-ee94-41ef-ada7-f5c9eb6ba208" class="">유아체육 파견 강사
(2018.10. ~ 2020.02.)</h3><ul id="2b5c76c6-f074-47bb-b714-28d15a8971ed" class="bulleted-list"><li style="list-style-type:disc">용산 아모레퍼시픽, 대림산업 한숲어린이집, 현대다솜 어린이집 파견강사</li></ul><ul id="418a2a70-e0bd-4339-a3f7-4e10f365e165" class="bulleted-list"><li style="list-style-type:disc">🖐Main role : 체육 수업, 이벤트 진행</li></ul><h3 id="f6fb597d-81d9-4256-9efd-7a2e0ca5025d" class="">사회복지공동모금회
(2016.09. ~ 2017.12.)</h3><ul id="0a1c09b1-18e5-4b67-b55f-31ebfd73373d" class="bulleted-list"><li style="list-style-type:disc">사회복지공동모금회 중앙회 내부행사 및 외부 대관 관리</li></ul><ul id="2f507ada-ed56-48df-a5ed-99612ce4f94b" class="bulleted-list"><li style="list-style-type:disc">🖐Main role : 대관 관리</li></ul><hr id="fab91703-e390-4232-bbec-a09e2a96a388"/><h1 id="ded172d0-1b16-4c36-8e5b-6bf4c885191f" class=""><mark class="highlight-orange">Skill.</mark></h1><ul id="6ec558d0-61d0-4342-958b-24689a6b4779" class="bulleted-list"><li style="list-style-type:disc">Front-End: HTML/CSS</li></ul><ul id="459b3e85-dee7-4887-9507-74826292346e" class="bulleted-list"><li style="list-style-type:disc">Back-End: Python, Tensorflow, Sckit-learn, AWS (EC2, Lambda, Gateway)</li></ul><ul id="f7efaf15-e0d5-4357-bb96-da66729c179d" class="bulleted-list"><li style="list-style-type:disc">Database: SQLite</li></ul><ul id="c63bcd24-8a77-4831-b252-8f33dc31ff07" class="bulleted-list"><li style="list-style-type:disc">Sub: Slack, Notion</li></ul><p id="bdadc762-6d73-419c-8373-ef8a8074e5a3" class="">
</p><hr id="e71e7f00-faa4-4191-a1d7-ea836724c1d3"/><h1 id="d5552088-0bcc-46f1-a8f0-ac981dd8817f" class=""><mark class="highlight-orange">Education.</mark></h1><h3 id="33fe6234-bee4-4e97-819b-d314299e4269" class="">42Seoul La Piscine (2021.10.04~2021.10.29)</h3><ul id="1f409d5a-2ac0-4552-8a43-33caccc87bf4" class="bulleted-list"><li style="list-style-type:disc">Linux Shell 기본, C 언어, 알고리즘 등</li></ul><h3 id="86e6748f-c66c-47fb-8e70-fd120f04018c" class="">멋쟁이 사자처럼 인공지능 통합과정
(2021.05.31~2021.08.13)</h3><ul id="a2081c55-6762-4a46-bac2-1f051b791393" class="bulleted-list"><li style="list-style-type:disc">Python 기반 EDA, Scraping, ML, DL, Web Development 등 수학</li></ul><ul id="d8a6bb6b-192d-4a82-ba99-3c955d5cb1d9" class="bulleted-list"><li style="list-style-type:disc">2개의 Project, 3개의 Semi-Project 진행</li></ul><hr id="41fb3e90-6817-420e-9da7-63c522f8c0b8"/><h3 id="6708bbd1-6b9a-41e3-b5c0-6ec55bbdcb57" class="">멋쟁이 사자처럼 가상자산 자동거래 시스템 만들기 with 고팍스
(2021.07.06)</h3><ul id="4a8899ad-32b1-414a-b3b7-897b591eccf2" class="bulleted-list"><li style="list-style-type:disc">Gopax API를 활용하여 AWS(EC2, Cloud9)로 자동 거래 시스템 구현</li></ul><hr id="dd3cbd33-c4f0-4c7e-905a-aa9047db4565"/><h2 id="e724e598-8a3f-40a1-97ad-199721931a1a" class=""><mark class="highlight-orange">Certification.</mark></h2><h3 id="21b3940c-3eb8-4103-b69b-f26d92eecf38" class="">GAIQ(2021. 11. 19)</h3><ul id="8656abf7-a4b9-427a-b482-1c3c89463a95" class="bulleted-list"><li style="list-style-type:disc">Google Analytics Individual Qualification</li></ul><p id="267569f4-3822-41ce-aecb-43cd200ce691" class="">
</p></div></article></body></html>