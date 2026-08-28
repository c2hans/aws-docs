---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/set-language-static-map.html
---

# How to set language for static maps
<a name="set-language-static-map"></a>

You can set the language for a static map, in case you don't want to use the default language.

In this example, a location in Tokyo which would generally default to Japanese text is requested in English, overwriting the regional default.

The example shows the response image for a request where language is provided, and one where the language is not provided. The corresponding labels reflect the difference between a map showing the requested language and a map that shows the default language.

------
#### [ Request URL - English set as the language ]

```
https://maps.geo.us-east-1.amazonaws.com/v2/static/map?center=139.4575,35.539&style=Standard&lang=en&height=700&width=700&zoom=14
```

------
#### [ Response image ]

![Static map of Tokyo with labels displayed in English, demonstrating the lang parameter override.](http://docs.aws.amazon.com/location/latest/developerguide/images/mapsV2/setLanguageEnglishStaticMap.png)

------

------
#### [ Request URL - default language ]

```
https://maps.geo.us-east-1.amazonaws.com/v2/static/map?center=139.4575,35.539&style=Standard&height=700&width=700&zoom=14
```

------
#### [ Response image ]

![Static map of Tokyo with labels displayed in the default language (Japanese), showing regional language behavior without the lang parameter.](http://docs.aws.amazon.com/location/latest/developerguide/images/mapsV2/setLanguageDefaultStaticMap.png)

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
