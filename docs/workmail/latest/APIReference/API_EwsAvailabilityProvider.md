---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_EwsAvailabilityProvider.html
---

# EwsAvailabilityProvider
<a name="API_EwsAvailabilityProvider"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Describes an EWS based availability provider. This is only used as input to the service.

## Contents
<a name="API_EwsAvailabilityProvider_Contents"></a>

 ** EwsEndpoint **   <a name="workmail-Type-EwsAvailabilityProvider-EwsEndpoint"></a>
The endpoint of the remote EWS server.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `https?://[A-Za-z0-9.-]+(:[0-9]+)?/.*`
Required: Yes

 ** EwsPassword **   <a name="workmail-Type-EwsAvailabilityProvider-EwsPassword"></a>
The password used to authenticate the remote EWS server.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: Yes

 ** EwsUsername **   <a name="workmail-Type-EwsAvailabilityProvider-EwsUsername"></a>
The username used to authenticate the remote EWS server.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\u0020-\u00FF]+`
Required: Yes

## See Also
<a name="API_EwsAvailabilityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/EwsAvailabilityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/EwsAvailabilityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/EwsAvailabilityProvider)
