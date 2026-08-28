---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/customize-http-request.html
---

# Customize HTTP requests to AWS
<a name="customize-http-request"></a>

The AWS SDK for SAP ABAP handles the process of creating an HTTP request, sending a payload, and receiving a response. You can customize the behavior or content of the HTTP request to meet your own IT requirements. The SDK defines enhancement spot `/AWS1/RT_EHN_HTTP_CLIENT` as a central place to enhance the HTTP communication. The enhancement spot supports adding HTTP headers to the request made to AWS.

## Implement an enhancement
<a name="implement-enhancement"></a>

SAP provides the following instructions for implementing an enhancement spot:
+ [Classic ABAP](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/5f/103a4280da9923e10000000a155106/frameset.htm)
+ [BTP ABAP](https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/creating-badi-implementations)

## Filter the enhancement
<a name="filter-enhancement"></a>

The enhancement spot supports multiple implementations that can be active simultaneously. You can filter the execution of the BAdi based on the following attributes, if you need to ensure that your enhancement runs only on calls to a specific AWS service or API action:
+ `TLA` - The three-letter abbreviation of the service, in uppercase letters.
+ `OPERATION` - The API action name. For example, the operation to get an object from an S3 bucket is [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html). The action name is case-sensitive and might not exactly match the ABAP method name.

## Code the enhancement
<a name="code-enhancement"></a>

The enhancement provides the following method.

### MODIFY\_REQ\_HEADERS
<a name="modify-req-headers"></a>

```
CHANGING CT_HEADERS TYPE /AWS1/RT_STRINGMAP_TT
```

You can append and modify headers in the `CT_HEADERS` internal table. We do not recommend modifying headers, as this alters data that the AWS service uses. Any headers that you add are ignored by the AWS service, but can be processed by your IT infrastructure, such as proxy servers or other middleware.

The enhancement spot is called before the calculation of authentication and telemetry headers, so these can't be modified by the enhancement.

The following is an example implementation.

```
METHOD /aws1/if_rt_badi_http_client~modify_req_headers.
  APPEND VALUE /aws1/rt_stringpair_ts( name = '{{x-test-example}}' value = '{{value}}' )
    TO ct_headers.
ENDMETHOD.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
