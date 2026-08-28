---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-disable-default-endpoint.html
---

# Disable the default endpoint for REST APIs
<a name="rest-api-disable-default-endpoint"></a>

By default, clients can invoke your API by using the `execute-api` endpoint that API Gateway generates for your API. To ensure that clients can access your API only by using a custom domain name, disable the default `execute-api` endpoint. Clients can still connect to your default endpoint, but they will receive a `403 Forbidden` status code. Disabling the default endpoint affects all stages of the API. This setting takes affect when you update any setting on any stage, such as updating the deployment on the stage.

The following procedure shows how to disable the default endpoint for a REST API.

------
#### [ AWS Management Console ]

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. On the main navigation pane, choose **API settings**.

1. Choose an API.

1. On **API details**, choose **Edit**.

1. For **Default endpoint**, select **Inactive**.

1. Choose **Save changes**.

1. On the main navigation pane, choose **Resources**.

1. Choose **Deploy API**.

1. Redeploy your API to a stage or update any setting on a stage for the update to take effect.

------
#### [ AWS CLI ]

The following [update-rest-api](https://docs.aws.amazon.com/cli/latest/reference/apigateway/update-rest-api.html) command disables the default endpoint:

```
aws apigateway update-rest-api \
    --rest-api-id {{abcdef123}} \
    --patch-operations op=replace,path=/disableExecuteApiEndpoint,value='True'
```

After you disable the default endpoint, you must deploy your API for the change to take effect.

The following [create-deployment](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-deployment.html) command creates a deployment and associates it with a stage:

```
aws apigateway create-deployment \
    --rest-api-id {{abcdef123}} \
    --stage-name {{dev}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
