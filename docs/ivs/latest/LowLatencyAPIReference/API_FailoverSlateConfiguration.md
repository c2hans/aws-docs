---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_FailoverSlateConfiguration.html
---

# FailoverSlateConfiguration
<a name="API_FailoverSlateConfiguration"></a>

Object specifying a failover slate configuration.

## Contents
<a name="API_FailoverSlateConfiguration_Contents"></a>

 ** arn **   <a name="ivs-Type-FailoverSlateConfiguration-arn"></a>
Failover-slate-configuration ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:failover-slate-configuration/[a-zA-Z0-9-]+`
Required: Yes

 ** state **   <a name="ivs-Type-FailoverSlateConfiguration-state"></a>
Current state of the failover slate configuration.
Type: String
Valid Values: `CREATING | CREATE_FAILED | CREATED | UPDATING`
Required: Yes

 ** activationThresholdSeconds **   <a name="ivs-Type-FailoverSlateConfiguration-activationThresholdSeconds"></a>
Number of seconds of ingest interruption before the failover slate activates. Default: `3`.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 5.
Required: No

 ** maxSlateDisplaySeconds **   <a name="ivs-Type-FailoverSlateConfiguration-maxSlateDisplaySeconds"></a>
Maximum number of seconds that the failover slate displays. Default: `60`.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 180.
Required: No

 ** minSlateDisplaySeconds **   <a name="ivs-Type-FailoverSlateConfiguration-minSlateDisplaySeconds"></a>
Minimum number of seconds that the failover slate displays after activation. Default: `3`.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 10.
Required: No

 ** name **   <a name="ivs-Type-FailoverSlateConfiguration-name"></a>
Failover-slate-configuration name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** tags **   <a name="ivs-Type-FailoverSlateConfiguration-tags"></a>
Tags attached to the resource. Array of 1-50 maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no service-specific constraints beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

## See Also
<a name="API_FailoverSlateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/FailoverSlateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/FailoverSlateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/FailoverSlateConfiguration)
