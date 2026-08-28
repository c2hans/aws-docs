---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_Endpoint.html
---

# Endpoint
<a name="API_dax_Endpoint"></a>

Represents the information required for client programs to connect to the endpoint for a DAX cluster.

## Contents
<a name="API_dax_Endpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Address **   <a name="DDB-Type-dax_Endpoint-Address"></a>
The DNS hostname of the endpoint.
Type: String
Required: No

 ** Port **   <a name="DDB-Type-dax_Endpoint-Port"></a>
The port number that applications should use to connect to the endpoint.
Type: Integer
Required: No

 ** URL **   <a name="DDB-Type-dax_Endpoint-URL"></a>
The URL that applications should use to connect to the endpoint. The default ports are 8111 for the "dax" protocol and 9111 for the "daxs" protocol.
Type: String
Required: No

## See Also
<a name="API_dax_Endpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/Endpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/Endpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/Endpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
