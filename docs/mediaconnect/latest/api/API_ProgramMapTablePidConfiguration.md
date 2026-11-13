---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ProgramMapTablePidConfiguration.html
---

# ProgramMapTablePidConfiguration
<a name="API_ProgramMapTablePidConfiguration"></a>

The configuration settings for the Program Map Table (PMT) Packet ID (PID).

## Contents
<a name="API_ProgramMapTablePidConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** passthrough **   <a name="mediaconnect-Type-ProgramMapTablePidConfiguration-passthrough"></a>
The PMT PID configuration that passes through the PMT PID from the source.
Type: [Passthrough](API_Passthrough.md) object
Required: No

 ** set **   <a name="mediaconnect-Type-ProgramMapTablePidConfiguration-set"></a>
The PMT PID to use for the router output. If you also set the PCR PID, the two values must be different.
Type: Integer
Valid Range: Minimum value of 32. Maximum value of 8190.
Required: No

## See Also
<a name="API_ProgramMapTablePidConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ProgramMapTablePidConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ProgramMapTablePidConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ProgramMapTablePidConfiguration)
