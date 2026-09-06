---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RuntimeEnvironment.html
---

# RuntimeEnvironment
<a name="API_RuntimeEnvironment"></a>

Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.

A runtime environment can be one of the following:
+  For Linux applications
  +  Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS`)
+  For Windows applications
  + Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022`)
  + Proton 10.0-4 (`Type=PROTON, Version=20260204`)
  + Proton 9.0-2 (`Type=PROTON, Version=20250516`)
  + Proton 8.0-5 (`Type=PROTON, Version=20241007`)
  + Proton 8.0-2c (`Type=PROTON, Version=20230704`)

## Contents
<a name="API_RuntimeEnvironment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Type **   <a name="gameliftstreams-Type-RuntimeEnvironment-Type"></a>
The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.
Type: String
Valid Values: `PROTON | WINDOWS | UBUNTU`
Required: Yes

 ** Version **   <a name="gameliftstreams-Type-RuntimeEnvironment-Version"></a>
Versioned container environment for the application operating system.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_RuntimeEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/RuntimeEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/RuntimeEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/RuntimeEnvironment)
