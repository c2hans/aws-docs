---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-service-servicedetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Service ServiceDetails
<a name="aws-properties-devopsagent-service-servicedetails"></a>

Service-specific configuration details provided during registration.

## Syntax
<a name="aws-properties-devopsagent-service-servicedetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-service-servicedetails-syntax.json"></a>

```
{
  "[AzureIdentity](#cfn-devopsagent-service-servicedetails-azureidentity)" : {{AzureIdentityServiceDetails}},
  "[Dynatrace](#cfn-devopsagent-service-servicedetails-dynatrace)" : {{DynatraceServiceDetails}},
  "[GitLab](#cfn-devopsagent-service-servicedetails-gitlab)" : {{GitLabDetails}},
  "[MCPServer](#cfn-devopsagent-service-servicedetails-mcpserver)" : {{MCPServerDetails}},
  "[MCPServerGrafana](#cfn-devopsagent-service-servicedetails-mcpservergrafana)" : {{MCPServerGrafanaDetails}},
  "[MCPServerNewRelic](#cfn-devopsagent-service-servicedetails-mcpservernewrelic)" : {{NewRelicServiceDetails}},
  "[MCPServerSigV4](#cfn-devopsagent-service-servicedetails-mcpserversigv4)" : {{MCPServerSigV4Details}},
  "[MCPServerSplunk](#cfn-devopsagent-service-servicedetails-mcpserversplunk)" : {{MCPServerSplunkDetails}},
  "[PagerDuty](#cfn-devopsagent-service-servicedetails-pagerduty)" : {{PagerDutyDetails}},
  "[ServiceNow](#cfn-devopsagent-service-servicedetails-servicenow)" : {{ServiceNowServiceDetails}}
}
```

### YAML
<a name="aws-properties-devopsagent-service-servicedetails-syntax.yaml"></a>

```
  [AzureIdentity](#cfn-devopsagent-service-servicedetails-azureidentity): {{
    AzureIdentityServiceDetails}}
  [Dynatrace](#cfn-devopsagent-service-servicedetails-dynatrace): {{
    DynatraceServiceDetails}}
  [GitLab](#cfn-devopsagent-service-servicedetails-gitlab): {{
    GitLabDetails}}
  [MCPServer](#cfn-devopsagent-service-servicedetails-mcpserver): {{
    MCPServerDetails}}
  [MCPServerGrafana](#cfn-devopsagent-service-servicedetails-mcpservergrafana): {{
    MCPServerGrafanaDetails}}
  [MCPServerNewRelic](#cfn-devopsagent-service-servicedetails-mcpservernewrelic): {{
    NewRelicServiceDetails}}
  [MCPServerSigV4](#cfn-devopsagent-service-servicedetails-mcpserversigv4): {{
    MCPServerSigV4Details}}
  [MCPServerSplunk](#cfn-devopsagent-service-servicedetails-mcpserversplunk): {{
    MCPServerSplunkDetails}}
  [PagerDuty](#cfn-devopsagent-service-servicedetails-pagerduty): {{
    PagerDutyDetails}}
  [ServiceNow](#cfn-devopsagent-service-servicedetails-servicenow): {{
    ServiceNowServiceDetails}}
```

## Properties
<a name="aws-properties-devopsagent-service-servicedetails-properties"></a>

`AzureIdentity`  <a name="cfn-devopsagent-service-servicedetails-azureidentity"></a>
Azure identity service configuration.
*Required*: No
*Type*: [AzureIdentityServiceDetails](aws-properties-devopsagent-service-azureidentityservicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dynatrace`  <a name="cfn-devopsagent-service-servicedetails-dynatrace"></a>
Dynatrace service configuration.
*Required*: No
*Type*: [DynatraceServiceDetails](aws-properties-devopsagent-service-dynatraceservicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GitLab`  <a name="cfn-devopsagent-service-servicedetails-gitlab"></a>
GitLab service configuration.
*Required*: No
*Type*: [GitLabDetails](aws-properties-devopsagent-service-gitlabdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServer`  <a name="cfn-devopsagent-service-servicedetails-mcpserver"></a>
Custom MCP server configuration.
*Required*: No
*Type*: [MCPServerDetails](aws-properties-devopsagent-service-mcpserverdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerGrafana`  <a name="cfn-devopsagent-service-servicedetails-mcpservergrafana"></a>
Grafana MCP server configuration.
*Required*: No
*Type*: [MCPServerGrafanaDetails](aws-properties-devopsagent-service-mcpservergrafanadetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerNewRelic`  <a name="cfn-devopsagent-service-servicedetails-mcpservernewrelic"></a>
New Relic MCP server configuration.
*Required*: No
*Type*: [NewRelicServiceDetails](aws-properties-devopsagent-service-newrelicservicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSigV4`  <a name="cfn-devopsagent-service-servicedetails-mcpserversigv4"></a>
SigV4-authenticated MCP server configuration.
*Required*: No
*Type*: [MCPServerSigV4Details](aws-properties-devopsagent-service-mcpserversigv4details.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MCPServerSplunk`  <a name="cfn-devopsagent-service-servicedetails-mcpserversplunk"></a>
Splunk MCP server configuration.
*Required*: No
*Type*: [MCPServerSplunkDetails](aws-properties-devopsagent-service-mcpserversplunkdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PagerDuty`  <a name="cfn-devopsagent-service-servicedetails-pagerduty"></a>
PagerDuty service configuration.
*Required*: No
*Type*: [PagerDutyDetails](aws-properties-devopsagent-service-pagerdutydetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceNow`  <a name="cfn-devopsagent-service-servicedetails-servicenow"></a>
ServiceNow service configuration.
*Required*: No
*Type*: [ServiceNowServiceDetails](aws-properties-devopsagent-service-servicenowservicedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
