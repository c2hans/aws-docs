---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-receiver-config.html
---

# Configure alert manager to send messages to your Amazon SNS topic
<a name="AMP-alertmanager-receiver-config"></a>

After you have a (new or existing) **Standard** type Amazon SNS topic, you can add it to your alert manager configuration as an alert receiver. Alert manager can forward your alerts to a configured alert receiver. To complete this, you must know the Amazon Resource Name (ARN) of your Amazon SNS topic.

For more information about Amazon SNS receiver configuration, see [<sns\_configs>](https://prometheus.io/docs/alerting/latest/configuration/#sns_configs) in the Prometheus configuration documentation.

**Unsupported properties**

Amazon Managed Service for Prometheus supports Amazon SNS as the alert receiver. However, because of service constraints, not all of the properties of the Amazon SNS receiver are supported. The following properties are not allowed in an Amazon Managed Service for Prometheus alert manager configuration file:
+ `api_url:` – Amazon Managed Service for Prometheus sets the `api_url` for you, so this property is not allowed.
+ `Http_config` – This property allows you to set external proxies. Amazon Managed Service for Prometheus does not currently support this feature.

Additionally, SigV4 settings are required to have a Region property. Without the Region property, Amazon Managed Service for Prometheus doesn't have enough information to make the authorization request.

**To configure alert manager with your Amazon SNS topic as the receiver**

1. If you are using an existing alert manager configuration file, open it in a text editor.

1. If there are current receivers other than Amazon SNS in the `receivers` block, remove them. You can configure multiple Amazon SNS topics to be receivers by putting them in separate `sns_config` blocks within the `receivers` block.

1. Add the following YAML block within the `receivers` section.

   ```
   - name: {{name_of_receiver}}
     sns_configs:
       - sigv4:
           region: {{AWS Region}}
         topic_arn: {{ARN_of_SNS_topic}}
         subject: {{yoursubject}}
         attributes:
           key: {{yourkey}}
           value: {{yourvalue}}
   ```

If a `subject`is not specified, by default, a subject would be generated with the default template with the label name and values, which may result in a value that is too long for SNS. To change the template that is applied to the subject, refer to [Configure alert manager to send messages to Amazon SNS as JSON](AMP-alertmanager-receiver-JSON.md) in this guide.

Now you must upload your alert manager configuration file to Amazon Managed Service for Prometheus. For more information, see [Upload your alert manager configuration file to Amazon Managed Service for Prometheus](AMP-alertmanager-upload.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
