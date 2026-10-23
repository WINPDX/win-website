body = open('win_preview.html','r',encoding='utf-8').read()
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Westside Interfaith Neighbors | Portland Westside Interfaith Coalition</title>
<meta name="description" content="Westside Interfaith Neighbors (WIN) is a coalition of 14 faith communities on Portland's westside - gathering for potlucks, prayer services, education, and service. Everyone is welcome.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://winpdx.org/">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="apple-touch-icon" href="images/logo.png">
<meta name="theme-color" content="#1b1b1b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Westside Interfaith Neighbors">
<meta property="og:title" content="Westside Interfaith Neighbors">
<meta property="og:description" content="A coalition of 14 faith communities on Portland's westside - potlucks, prayer services, education, and service. Everyone is welcome.">
<meta property="og:url" content="https://winpdx.org/">
<meta property="og:image" content="https://winpdx.org/images/share-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Westside Interfaith Neighbors">
<meta name="twitter:description" content="A coalition of 14 faith communities on Portland's westside. Everyone is welcome.">
<meta name="twitter:image" content="https://winpdx.org/images/share-card.png">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"NGO","name":"Westside Interfaith Neighbors","alternateName":"WIN","url":"https://winpdx.org/","logo":"https://winpdx.org/images/logo.png","description":"A coalition of 14 faith communities on Portland's westside, gathering for potlucks, prayer services, education, and service.","areaServed":"Portland Westside, Oregon"}</script>
<style>:root{color-scheme:light}*{box-sizing:border-box}html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
out = head + body + '\n</body>\n</html>\n'
open('/mnt/user-data/outputs/index.html','w',encoding='utf-8').write(out)
print('wrote', len(out), 'bytes')
