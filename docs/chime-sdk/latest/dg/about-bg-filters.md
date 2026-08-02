---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/about-bg-filters.html
---

# About using background filters for the Amazon Chime SDK
<a name="about-bg-filters"></a>

Background filters can be CPU-intensive and GPU-intensive. Some mobile devices and lower-specification laptop or desktop computers may not have the power to run the filters along with multiple video streams.

## SIMD support for the Amazon Chime SDK
<a name="simd-support"></a>

Background filters are more efficient in environments that support Single Instruction, Multiple Data (SIMD). The filters use less CPU for a given complexity level when you enable SIMD. Low-powered devices running browsers without SIMD support may not run background filters.

## WebGL2 support for the Amazon Chime SDK
<a name="webgl2-support"></a>

The `VideoFxProcessor` object requires browsers that support WebGL2 in order to access the GPU on the client device.

## Content delivery and bandwidth for the Amazon Chime SDK
<a name="delivery-caching-bandwidth"></a>

An Amazon content delivery network loads the machine-learning-model files for background filters at runtime. This provides low-latency global distribution without the need to serve a full suite of files as part of your application. However, loading model files can add latency to parts of your application. To help mitigate that impact, browsers cache the model files indefinitely. That cache makes subsequent loads significantly faster. As a best practice, check for supported browsers, then create the background filter resources when users may not notice any latency. For example, you can download model files while users wait in a lobby, or while they use a device picker.

Your application must connect to the following:
+ Amazon Chime SDK media services.
+ Amazon CloudFront via HTTPS (port 443).

All requests are to subdomains of `sdkassets.chime.aws`. Applications that can't access the content delivery network or don't include the correct domain in their [content security policy](content-security.md) will fail their support checks and be unable to use the filters.

For more information about CloudFront’s IP address ranges, see [ Locations and IP address ranges of CloudFront edge servers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html) in the *Amazon CloudFront Developer Guide*.

## Browser compatibility for the Amazon Chime SDK
<a name="filters-browser-compat"></a>

The following table lists the browsers and version that support background filters.

| Browser | Minimum supported version |
| --- | --- |
| Firefox | 76\+ |
| Chromium-based browsers and environments, including Edge and Electron | 78\+ |
| Android Chrome | 110\+ |
| Safari on macOS | 16.3\+ |
| Safari on iOS (iPhone, iPad) | 16.x |
| Chrome on iOS | 110.0.0.x.x |
| Firefox on iOS (iPhone iPad) | 16.x |

Version 3.14 of the `VideoFxProcessor` object supports Android. For Android device support on versions prior to 3.14, use the `BackgroundBlurVideoFrameProcessor` and `BackgroundReplacementVideoFrameProcessor` objects. For more information about using them, refer to the [https://aws.github.io/amazon-chime-sdk-js/modules/backgroundfilter_video_processor.html](https://aws.github.io/amazon-chime-sdk-js/modules/backgroundfilter_video_processor.html) page on GitHub.
