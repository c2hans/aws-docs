---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_Sample.html
---

# Sample
<a name="API_Sample"></a>

Represents a sample of performance data.

## Contents
<a name="API_Sample_Contents"></a>

 ** arn **   <a name="devicefarm-Type-Sample-arn"></a>
The sample's ARN.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** type **   <a name="devicefarm-Type-Sample-type"></a>
The sample's type.
Must be one of the following values:
+ CPU: A CPU sample type. This is expressed as the app processing CPU time (including child processes) as reported by process, as a percentage.
+ MEMORY: A memory usage sample type. This is expressed as the total proportional set size of an app process, in kilobytes.
+ NATIVE\_AVG\_DRAWTIME
+ NATIVE\_FPS
+ NATIVE\_FRAMES
+ NATIVE\_MAX\_DRAWTIME
+ NATIVE\_MIN\_DRAWTIME
+ OPENGL\_AVG\_DRAWTIME
+ OPENGL\_FPS
+ OPENGL\_FRAMES
+ OPENGL\_MAX\_DRAWTIME
+ OPENGL\_MIN\_DRAWTIME
+ RX
+ RX\_RATE: The total number of bytes per second (TCP and UDP) that are sent, by app process.
+ THREADS: A threads sample type. This is expressed as the total number of threads per app process.
+ TX
+ TX\_RATE: The total number of bytes per second (TCP and UDP) that are received, by app process.
Type: String
Valid Values: `CPU | MEMORY | THREADS | RX_RATE | TX_RATE | RX | TX | NATIVE_FRAMES | NATIVE_FPS | NATIVE_MIN_DRAWTIME | NATIVE_AVG_DRAWTIME | NATIVE_MAX_DRAWTIME | OPENGL_FRAMES | OPENGL_FPS | OPENGL_MIN_DRAWTIME | OPENGL_AVG_DRAWTIME | OPENGL_MAX_DRAWTIME`
Required: No

 ** url **   <a name="devicefarm-Type-Sample-url"></a>
The presigned Amazon S3 URL that can be used with a GET request to download the sample's file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

## See Also
<a name="API_Sample_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/Sample)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/Sample)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/Sample)
