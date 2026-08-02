---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-remove.html
---

# Result when removing color space metadata
<a name="colorspace-output-remove"></a>

Read this section if you set up one or more MediaLive outputs to [pass through the color space](colorspace-output-setup.md#colorspace-output-setup-passthrough) or [convert the color space](colorspace-output-setup.md#colorspace-output-setup-convert) and you chose to remove the color space metadata. The following table shows how MediaLive handles each type of color space that it encounters in the source.

|  Color space that MediaLive encounters  |  How MediaLive handles the color space  |
| --- | --- |
| Content in any color space that MediaLive supports<br />Content with no color space metadata | [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-remove.html)The output won't contain any color space metadata, brightness metadata, or display metadata. |
| Content marked with an unknown or unsupported color space | We can't make any promises about how MediaLive will handle input that is in an unsupported color space. Any of the following might apply:[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-remove.html) |
