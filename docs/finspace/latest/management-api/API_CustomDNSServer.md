---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CustomDNSServer.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CustomDNSServer
<a name="API_CustomDNSServer"></a>

A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.

## Contents
<a name="API_CustomDNSServer_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** customDNSServerIP **   <a name="finspace-Type-CustomDNSServer-customDNSServerIP"></a>
The IP address of the DNS server.
Type: String
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`
Required: Yes

 ** customDNSServerName **   <a name="finspace-Type-CustomDNSServer-customDNSServerName"></a>
The name of the DNS server.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$`
Required: Yes

## See Also
<a name="API_CustomDNSServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CustomDNSServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CustomDNSServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CustomDNSServer)
