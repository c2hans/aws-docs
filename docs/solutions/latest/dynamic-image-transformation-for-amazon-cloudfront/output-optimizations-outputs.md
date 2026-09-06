---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/output-optimizations-outputs.html
---

# Output optimizations (`outputs`)
<a name="output-optimizations-outputs"></a>

The `outputs` array configures auto-optimization. Each `type` (`quality`, `format`, `autosize`) can appear at most once. Each output accepts an optional `fallback` object that defines the value used when device detection cannot determine the browser’s capabilities.

```
{
  "outputs": [
    {
      "type": "quality",
      "value": [77, [0, 1, 50], [1, 2, 75], [2, 5, 90]],
      "fallback": { "dpr": 1.0 }
    },
    {
      "type": "format",
      "value": "auto",
      "fallback": { "format": "jpeg" }
    },
    {
      "type": "autosize",
      "value": [320, 480, 640, 960, 1440, 1920],
      "fallback": { "viewportWidth": 1920 }
    }
  ]
}
```

| Output |  `value`  |  `fallback`  |
| --- | --- | --- |
|  `quality`  | An array whose first element is the default quality integer (1-100), followed by `[minDpr, maxDpr, quality]` mapping entries. The leading default-quality integer is required. |  `{ "dpr": <1.0-5.0> }`: the device pixel ratio used to select a quality level when no DPR signal is available. |
|  `format`  |  `auto`, or one of `jpg`, `jpeg`, `png`, `tiff`, `webp`, `gif`, `avif`. |  `{ "format": <one of the format values> }`: the format used when `auto` cannot determine browser support. |
|  `autosize`  | An array of one or more derivative widths (positive integers). |  `{ "viewportWidth": <320-3840> }`: the viewport width used when no viewport signal is available. |

The `fallback` object is optional on every output; policies without it remain valid.
