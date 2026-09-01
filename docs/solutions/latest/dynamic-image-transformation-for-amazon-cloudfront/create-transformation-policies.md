---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-transformation-policies.html
---

# Create transformation policies
<a name="create-transformation-policies"></a>

Transformation policies define how images are processed. A policy contains two kinds of instructions: **transformations** (operations such as resize, format, quality, blur, or smart crop, each optionally gated by a condition) and **outputs** (the device-aware optimizations `quality`, `format`, and `autosize`). You can create policies using either the Admin UI form or by providing JSON configuration directly. A policy can be marked as the default, in which case it applies to requests that match a mapping with no policy attached.

 **Navigation:** In the Admin UI left navigation, select **Transformation policies**, and then choose **Create policy**.

## Using the Admin UI
<a name="using-the-admin-ui"></a>

1. In the Admin UI, select **Transformation policies**, and then choose **Create policy**.

1. Provide the policy details:
   +  **Policy Name**: A unique name, 1-100 characters, using letters, numbers, spaces, underscores, or hyphens.
   +  **Description (Optional)**: A description of what the policy does.
   +  **Set as default policy**: Select this checkbox to make the policy apply to requests whose mapping has no policy attached.

1. Configure transformations using the UI:
   + Choose **Add Transformation** to add an image processing operation.
   + Select the transformation type (resize, format, quality, smart crop, and so on).
   + Configure the transformation parameters using the form fields. Optionally add a condition so the transformation applies only when a request header matches a value.

1. Configure outputs using the UI:
   + Choose **Add Output** to define a device-aware optimization.
   + Select the output type (`quality`, `format`, or `autosize`). Each output type can be added only once.
   + Configure the output parameters, including the optional `fallback` value used when device detection cannot determine the browser’s capabilities.

1. Choose **Save** to create the policy.

The following worked examples show the two most common policy shapes, expressed as the values you enter in the Create policy form.

**Example 1: Optimization policy (format \+ quality \+ autosize)**
This policy automatically serves the most efficient format and resolution for each requesting device. It contains only outputs (no transformations). Choose **Add Output** once for each row below:

| Output | Configuration | Fallback |
| --- | --- | --- |
| Format |  **Format Selection**: `Auto (recommended)` — serves WebP or AVIF to browsers that support them |  **Fallback Format**: `JPEG`  |
| Quality |  **Default Quality**: `77`. **DPR Rules**: `0–1` → `50`, `1–2` → `75`, `2+` → `90`  |  **Fallback DPR**: `1.0`  |
| Autosize | Enabled; responsive widths are applied automatically |  **Fallback Viewport Width**: `1920`  |

**Example 2: Conditional transformation policy**
This policy applies a transformation only when a request carries a specific header. Each transformation can include an optional condition: a request header to inspect and a value to match. Here, images are flipped only when the request includes the header `x-flip: true`. Choose **Add Transformation** once for each row below:

| Transformation | Configuration | Condition |
| --- | --- | --- |
| Resize |  **Width**: `800`; **Fit Mode**: `Contain`  |  *(none)*  |
| Flip | Enabled | Applies only when the request header `x-flip` equals `true`  |

 **Screenshot of the Create policy form in the Admin UI, configuring the quality output optimization.**

![Admin UI Create policy form showing quality output configuration](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/admin-ui-create-policy-1.png)

 **Screenshot of the Create policy form in the Admin UI, showing the optimization policy fully configured with all three output optimizations (format, quality, and autosize).**

![Admin UI Create policy form with output optimizations configured](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/admin-ui-create-policy-2.png)

## Using Management API
<a name="using-management-api"></a>

Alternatively, you can create policies by providing JSON configuration directly using the Management API:

1. In the Admin UI, navigate to the **Policies** section.

1. Choose **Create Policy** and provide:
   +  **Policy Name**: Descriptive name for the policy
   +  **Description**: Optional description
   +  **Policy JSON**: JSON configuration defining transformations and outputs

1. Example policy JSON. This reference example exercises the full range of available operations: the `outputs` array defines device-aware format, quality, and autosize optimizations, and the `transformations` array applies image edits (some gated by a `condition`). A real policy typically uses a small subset of these:

   ```
   {
       "outputs": [
           {
               "type" : "quality",
               "value" : [
                   77,
                   [0,1,50],
                   [1,2,75],
                   [2,500,90]
               ],
               "fallback": { "dpr": 1.0 }
           },
           {
               "type": "format",
               "value": "auto",
               "fallback": { "format": "jpeg" }
           },
           {
               "type": "autosize",
               "value": [320,480,640,960,1440,1920],
               "fallback": { "viewportWidth": 1920 }
           }
       ],
       "transformations": [
           {
               "transformation": "blur",
               "value": 7
           },
           {
               "transformation": "convolve",
               "value": {
                   "width": 3,
                   "height": 3,
                   "kernel": [1,0,-1,0,0,0,-1,0,1]
               }
           },
           {
               "transformation": "extract",
               "value": [10,10,100,100]
           },

           {
               "transformation": "flip",
               "value": true,
               "condition" : {
                   "field": "header.XYZ",
                   "value": "ABC"
               }
           },
           {
               "transformation": "flop",
               "value": false
           },
           {
               "transformation": "grayscale",
               "value": true
           },
           {
               "transformation": "normalize",
               "value": true
           },
           {
               "transformation": "resize",
               "value": {
                   "width": 400,
                   "height": 600,
                   "fit": "contain"
               }
           },
           {
               "transformation": "rotate",
               "value": 60,
               "condition" : {
                   "field": "header.XYZ",
                   "value": "ABC"
               }
           },
           {
               "transformation": "sharpen",
               "value": {
                   "sigma": 5
               }
           },
           {
               "transformation": "smartCrop",
               "value": true
           },

           {
               "transformation": "stripExif",
               "value": true
           },
           {
               "transformation": "stripIcc",
               "value": true
           },
           {
               "transformation": "tint",
               "value": "blue"
           },
           {
               "transformation": "watermark",
               "value": [ "watermarkURL", [15, 15, 0.1, 0.4, 0.4]]
           }
       ]
   }
   ```

1. Choose **Save** to create the policy.

**Note**
 **Output fallbacks (ECS architecture only, v8.1\+).** The `quality`, `format`, and `autosize` outputs accept an optional `fallback` object that defines the value DIT uses when device detection cannot determine the browser’s capabilities:
 `quality`: `fallback.dpr` (1.0-5.0) is the device pixel ratio used to select a quality level when no DPR signal is available. The `value` array still begins with a default quality integer (the first element), followed by `[minDpr, maxDpr, quality]` mapping entries.
 `format`: `fallback.format` (`jpg`, `jpeg`, `png`, `tiff`, `webp`, `gif`, `avif`) is the format used when `auto` cannot determine browser support.
 `autosize`: `fallback.viewportWidth` (320-3840) is the viewport width used when no viewport signal is available.
The `fallback` object is optional; existing policies without it remain valid.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
