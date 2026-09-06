---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_BatchGetRouterNetworkInterfaceError.html
---

# BatchGetRouterNetworkInterfaceError
<a name="API_BatchGetRouterNetworkInterfaceError"></a>

An error that occurred when retrieving multiple router network interfaces in the BatchGetRouterNetworkInterface operation, including the ARN, error code, and error message.

## Contents
<a name="API_BatchGetRouterNetworkInterfaceError_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-BatchGetRouterNetworkInterfaceError-arn"></a>
The Amazon Resource Name (ARN) of the router network interface for which the error occurred.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** code **   <a name="mediaconnect-Type-BatchGetRouterNetworkInterfaceError-code"></a>
The error code associated with the error.
Type: String
Required: Yes

 ** message **   <a name="mediaconnect-Type-BatchGetRouterNetworkInterfaceError-message"></a>
A message describing the error.
Type: String
Required: Yes

## See Also
<a name="API_BatchGetRouterNetworkInterfaceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/BatchGetRouterNetworkInterfaceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/BatchGetRouterNetworkInterfaceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/BatchGetRouterNetworkInterfaceError)
