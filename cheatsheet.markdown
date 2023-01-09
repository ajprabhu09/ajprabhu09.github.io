---
layout: page
title: Cheatsheets
permalink: /cheatsheets/
---
{%- if site.cheatsheets.size > 0 -%}
<ul class="post-list">
  {%- for post in site.cheatsheets -%}
  <li>
    <h3>
      <a class="post-link" href="{{ post.url | relative_url }}">
        {{ post.title | escape }}
      </a>
    </h3>
    {%- if site.show_excerpts -%}
      {{ post.excerpt }}
    {%- endif -%}
  </li>
  {%- endfor -%}
</ul>

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
{%- endif -%}