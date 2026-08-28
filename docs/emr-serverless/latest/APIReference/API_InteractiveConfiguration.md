---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_InteractiveConfiguration.html
---

# InteractiveConfiguration
<a name="API_InteractiveConfiguration"></a>

The configuration to use to enable the different types of interactive use cases in an application.

## Contents
<a name="API_InteractiveConfiguration_Contents"></a>

 ** livyEndpointEnabled **   <a name="emrserverless-Type-InteractiveConfiguration-livyEndpointEnabled"></a>
Enables an Apache Livy endpoint that you can connect to and run interactive jobs.
Type: Boolean
Required: No

 ** sessionEnabled **   <a name="emrserverless-Type-InteractiveConfiguration-sessionEnabled"></a>
Enables interactive sessions on the application. When set to `true`, you can start interactive sessions using the `StartSession` operation.
Type: Boolean
Required: No

 ** studioEnabled **   <a name="emrserverless-Type-InteractiveConfiguration-studioEnabled"></a>
Enables you to connect an application to Amazon EMR Studio to run interactive workloads in a notebook.
Type: Boolean
Required: No

## See Also
<a name="API_InteractiveConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/InteractiveConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/InteractiveConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/InteractiveConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
