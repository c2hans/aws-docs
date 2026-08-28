---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/create-transformation-policies.html
---

# Create transformation policies
<a name="create-transformation-policies"></a>

Transformation policies define how images are processed based on conditions. You can create policies using either the Admin UI interface or by providing JSON configuration directly.

## Using the Admin UI
<a name="using-the-admin-ui"></a>

1. In the Admin UI, navigate to the **Policies** section.

1. Click **Create Policy** and provide:
   +  **Policy Name**: Descriptive name for the policy
   +  **Description**: Optional description of what the policy does

1. Configure transformations using the UI:
   + Click **Add Transformation** to add image processing operations
   + Select transformation type (resize, format, quality, etc.)
   + Configure transformation parameters using the form fields

1. Configure outputs using the UI:
   + Click **Add Output** to define output specifications
   + Select output type (quality, format, autosize)
   + Configure output parameters using the form fields

1. Click **Save** to create the policy.

## Using Management API
<a name="using-management-api"></a>

Alternatively, you can create policies by providing JSON configuration directly using the Management API:

1. In the Admin UI, navigate to the **Policies** section.

1. Click **Create Policy** and provide:
   +  **Policy Name**: Descriptive name for the policy
   +  **Description**: Optional description
   +  **Policy JSON**: JSON configuration defining transformations and outputs

1. Example policy JSON:

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
               ]
           },
           {
               "type": "format",
               "value": "auto"
           },
           {
               "type": "autosize",
               "value": [320,480,640,960,1440,1920]
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

1. Click **Save** to create the policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
