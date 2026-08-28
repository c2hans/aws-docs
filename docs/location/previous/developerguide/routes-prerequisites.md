---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/routes-prerequisites.html
---

# Prerequisites for calculating routes using Amazon Location
<a name="routes-prerequisites"></a>

This page outlines prerequisites to get started with the service's routing features, which enable you to calculate optimized routes and travel times between multiple locations. It covers essential topics, such as configuring access permissions, setting up the required resources within your AWS account, and any additional dependencies or tools needed based on your specific use case or development environment.

## Create a route calculator resource
<a name="create-route-calculator-resource"></a>

Before you can calculate a route, create a route calculator resource in your AWS account.

When you create a route calculator resource, you can choose from the data providers available:

1. **Esri** – For more information about Esri's coverage in your region of interest, see [Esri details on street networks and traffic coverage](https://doc.arcgis.com/en/arcgis-online/reference/network-coverage.htm).

1. **HERE Technologies** – For more information about HERE's coverage in your region of interest, see [HERE car routing coverage](https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/car-routing.html) and [HERE truck routing coverage](https://developer.here.com/documentation/routing-api/dev_guide/topics/coverage/truck-routing.html).

1. **Grab** – For more information about Grab's coverage, see [Countries/regions and area covered](grab.md#grab-coverage-area).

**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

You can do this using the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To create a route calculator resource using the Amazon Location console**

1. Open the Amazon Location console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. In the left navigation pane, choose **Route calculators**.

1. Choose **Create route calculator**.

1. Fill out the following boxes:
   + ****Name **** – Enter a name for the route calculator resource. For example, {{ExampleCalculator}}. Maximum 100 characters. Valid entries include alphanumeric characters, hyphens, periods, and underscores.
   + ****Description** ** – Enter an optional description.

1. For **Data providers**, choose a [data provider](https://aws.amazon.com/location/data-providers/) to use as a route calculator.

1. (Optional) Under **Tags**, enter a tag **Key** and **Value**. This adds a tag your new route calculator resource. For more information, see [Tagging your resources](tagging.md).

1. Choose **Create route calculator**.

------
#### [ API ]

**To create a route calculator resource using the Amazon Location APIs**

Use the `[CreateRouteCalculator](https://docs.aws.amazon.com/location-routes/latest/APIReference/API_CreateRouteCalculator.html)` operation from the Amazon Location Places APIs.

The following example is an API request to create a route calculator resource called {{ExampleCalculator}} using the data provider {{Esri}}.

```
POST /routes/v0/calculators
Content-type: application/json

{
   "CalculatorName": "{{ExampleCalculator}}",
   "DataSource": "{{Esri}}",
   "Description": "string",
   "Tags": {
      "Tag1" : "Value1"
   }
}
```

------
#### [ AWS CLI ]

**To create a route calculator resource using AWS CLI commands**

Use the `create-route-calculator` command.

The following example creates a route calculator resource called {{ExampleCalculator}} using {{Esri}} as the data provider.

```
aws location \
  create-route-calculator \
  --calculator-name "{{ExampleCalculator}}" \
  --data-source "{{Esri}}" \
  --tags Tag1=Value1
```

------

**Note**
Billing depends on your usage. You may incur fees for the use of other AWS services. For more information, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/).

## Authenticating your requests
<a name="routes-identity-pool"></a>

Once you create a route calculator resource and you're ready to begin building location features into your application, choose how you would authenticate your requests:
+ To explore ways you can access the services, see [Accessing Amazon Location Service](how-to-access.md).
+ If you have a website with anonymous users, you may want to use API Keys or Amazon Cognito.

  **Example**

  The following example shows using an API key for authorization, using [AWS JavaScript SDK v3](https://aws.amazon.com/sdk-for-javascript/), and the Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md).

  ```
  import { LocationClient, CalculateRouteCommand } from "@aws-sdk/client-location";
  import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";

  const apiKey = "{{v1.public.your-api-key-value}}"; // API key

  // Create an authentication helper instance using an API key
  const authHelper = await withAPIKey(apiKey);

  const client = new LocationClient({
    region: "{{<region>}}", // region containing Cognito pool
    ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
  });

  const input = {
    CalculatorName: "{{ExampleCalculator}}",
    DeparturePosition: [-123.4567, 45.6789],
    DestinationPosition: [-123.123, 45.234],
  };

  const command = new CalculateRouteCommand(input);

  const response = await client.send(command);
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
