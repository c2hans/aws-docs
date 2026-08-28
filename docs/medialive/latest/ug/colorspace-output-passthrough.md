---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-passthrough.html
---

# Result when passing through color space
<a name="colorspace-output-passthrough"></a>

Read this section if you set up one or more MediaLive outputs to [pass through the color space](colorspace-output-setup.md#colorspace-output-setup-passthrough). The following table shows how MediaLive handles each type of color space that it encounters in the source.

|  Color space that MediaLive encounters  |  How MediaLive handles the color space  |
| --- | --- |
| Content in any color space that MediaLive supports | Doesn't touch the color space or brightness (the pixel values) in the output.<br />Passes through any of the three sets of metadata that are present. |
| Content in a color space that MediaLive supports, but that isn't supported for the output codec. | This conversion isn't supported. After conversion, the color map of the content will be completely wrong. |
| Content marked with unknown or an unsupported color space | Doesn't touch the color space or brightness (the pixel values) in the output.<br />Leaves the content as marked with the unknown color space. <br />Passes through any brightness metadata and display metadata. |
| Content with no color space metadata | Doesn't touch the color space or brightness (the pixel values) in the output.<br />Leaves the content as unmarked (no color space metadata). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
