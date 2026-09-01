---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/ecs-playground.html
---

# Use the Playground
<a name="ecs-playground"></a>

**Note**
 **Supported in:** ECS architecture only (v8.1\+).

The Playground is an interactive interface for trying transformations against your deployment without writing code. It is hosted within the Admin UI and shares the same Cognito authentication, so you must sign in to the Admin UI before using it.

1. In the Admin UI, open the **Playground**.

1. In the **Image Path** field, enter a path that resolves through at least one of your configured mappings (for example, `/images/photo.jpg`). The path is appended to the image processing domain shown beneath the field, so the request matches a mapping and fetches the corresponding origin object.

1. Apply transformations to the request, either explicitly or by letting the matched mapping’s policy do it for you:

   1. To override the policy, set transformations directly under **Transformations**. These are sent as URL query parameters and take precedence over the policy’s transformation of the same type.

   1. To simulate client conditions, expand **Client Hint Presets** under **Output Optimizations** and select a **Device** and **Browser Format Support** preset. These send client hint headers (device pixel ratio, viewport width, and `Accept`) that the transformation policy reads to apply format negotiation, quality, and responsive sizing.

   1. If you make no changes here, the policy from the matched mapping is applied automatically.

1. View the transformed image alongside its extended transformation metrics, including pre- and post-optimization dimensions, file sizes, and formats; the resulting size reduction and compression ratio; and a processing-time breakdown covering origin fetch, transformation, and total server time.

 **Screenshot of the Playground showing a transformed image with its extended-metrics overlay.**

![Playground UI showing a transformed image with metrics overlay](http://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/images/playground-ui-example.png)

The Playground routes requests through the deployed DIT instance, so results reflect production behavior. Extended metrics are returned only for authenticated Playground sessions; if metrics stop appearing, refresh your Admin UI session to obtain a current Cognito token.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
