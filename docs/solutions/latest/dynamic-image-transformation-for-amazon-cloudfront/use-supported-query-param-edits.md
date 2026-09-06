---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/use-supported-query-param-edits.html
---

# Use supported Query Parameter edits
<a name="use-supported-query-param-edits"></a>

The solution supports the definition of certain image edits through the use of query parameters. These query parameters can be used by themselves, or in conjunction with base64 or Thumbor-style edits. For example

```
https://<ApiEndpoint>/<image.jpeg>?format=<FormatType>
```

```
https://<ApiEndpoint>/<base64EncodedRequest>?format=<FormatType>
```

```
https://<ApiEndpoint>/<modification>/<image.jpeg>?format=<FormatType>
```

If a query parameter includes an edit already included in the request, it will overwrite the included value.

The following query parameter edits are currently available:

| Query parameter name | Description | Options | Default |
| --- | --- | --- | --- |
|  ** [format](https://sharp.pixelplumbing.com/api-output#toformat) **  | Sets the output to the provided format | jpg, jpeg, heic, png, raw, tiff, webp, gif, avif | None |
|  ** [fit](https://sharp.pixelplumbing.com/api-resize#resize) **  | The method that should be used when resizing | cover, contain, fill, inside, outside | cover |
|  ** [width](https://sharp.pixelplumbing.com/api-resize#resize) **  | The width in pixels, the image should be resized to. | Positive integer or 0 | None |
|  ** [height](https://sharp.pixelplumbing.com/api-resize#resize) **  | The height in pixels, the image should be resized to. | Positive integer or 0 | None |
|  ** [rotate](https://sharp.pixelplumbing.com/api-operation#rotate) **  | The number of degrees the image should be rotated | 0-359 or blank (for null) | None |
|  ** [flip](https://sharp.pixelplumbing.com/api-operation#flip) **  | Mirror the image vertically | True/False | False |
|  ** [flop](https://sharp.pixelplumbing.com/api-operation#flop) **  | Mirror the image horizontally | True/False | False |
|  ** [greyscale](https://sharp.pixelplumbing.com/api-colour#greyscale) **  | Convert to 8-bit greyscale | True/False | False |
