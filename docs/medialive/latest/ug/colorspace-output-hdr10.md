---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html
---

# Result when converting color space to HDR10
<a name="colorspace-output-hdr10"></a>

Read this section if you set up one or more MediaLive outputs to [convert the color space](colorspace-output-setup.md#colorspace-output-setup-convert) to HDR10. The following table shows how MediaLive handles each type of color space that it encounters in the source.

|  Color space that MediaLive encounters  |  How MediaLive handles the color space  |
| --- | --- |
| Content in an SDR color space | [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html)This conversion fits the smaller SDR color space into the larger HDR color space and maps the pixels to new code values that represent the same color. <br />The conversion doesn't actually make the existing color richer. However, the bright parts of the content are brighter, and the dark parts are darker. |
| Content in HDR10 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html)  |
| Content in HLG |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html)  |
| Content in Dolby Vision 8.1 | This conversion isn't supported. After conversion, the color map of the content could be completely wrong. |
| Content marked with an unknown or unsupported color space | We can't make any promises about how MediaLive will handle source content that is in an unsupported color space. Any of the following might apply:[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html) |
| Content with no color space metadata |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/colorspace-output-hdr10.html)  |
