---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/places-prerequisites.html
---

# Places prerequisites using Amazon Location
<a name="places-prerequisites"></a>

Before you begin geocoding, reverse geocoding or searching for places, follow the prerequisite steps:

**Topics**
+ [Creating a place index resource](#create-place-index-resource)
+ [Authenticating your requests](#places-identity-pool)

## Creating a place index resource
<a name="create-place-index-resource"></a>

Begin by creating a place index resource in your AWS account.

When you create a place index resource, you can choose from the data providers available to support queries for geocoding, reverse geocoding, and searches:

1. **Esri **– For more information about Esri's coverage in your region of interest, see [Esri geocoding coverage](https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm) in the Esri documentation.

1. **HERE Technologies** – For more information about HERE's coverage in your region of interest, see [HERE geocoding coverage](https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html) in the HERE documentation.

1. **Grab** – Grab provides data only for Southeast Asia. For more information about Grab's coverage, see [Countries/regions and area covered](grab.md#grab-coverage-area) in this guide.

You can do this using the Amazon Location Service console, the AWS CLI, or the Amazon Location APIs.

------
#### [ Console ]

**To create a place index resource using the Amazon Location Service console**

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. In the left navigation pane, choose **Place indexes**.

1. Choose **Create place index**.

1. Fill out the following boxes:
   + ****Name **** – Enter a name for the place index resource. For example, {{ExamplePlaceIndex}}. Maximum 100 characters. Valid entries include alphanumeric characters, hyphens, periods, and underscores.
   + ****Description** ** – Enter an optional description.

1. Under **Data providers**, choose an available [data provider](https://aws.amazon.com/location/data-providers/) to use with your place index resource.
**Note**
If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the [AWS service terms](https://aws.amazon.com/service-terms) for more details.

1. Under **Data storage options**, specify if you intend to store search results from your place index resource.

1. (Optional) Under **Tags**, enter a tag **Key** and **Value**. This adds a tag your new place index resource. For more information, see [Tagging your resources](tagging.md).

1. Choose **Create place index**.

------
#### [ API ]

**To create a place index resource using the Amazon Location APIs**

Use the `[CreatePlaceIndex](https://docs.aws.amazon.com/location-places/latest/APIReference/API_CreatePlaceIndex.html)` operation from the Amazon Location Places APIs.

The following example is an API request to create a place index resource called {{ExamplePlaceIndex}} using the data provider {{Esri}}.

```
POST /places/v0/indexes
Content-type: application/json

{
   "DataSource": "{{Esri}}",
   "DataSourceConfiguration": {
      "IntendedUse": "{{SingleUse}}"
   },
   "Description": "string",
   "IndexName": "{{ExamplePlaceIndex}}",
   "Tags": {
      "Tag1" : "Value1"
   }
}
```

------
#### [ AWS CLI ]

**To create a place index resource using AWS CLI commands**

Use the `[create-place-index](https://docs.aws.amazon.com/cli/latest/reference/location/create-place-index.html)` command.

The following example creates a place index resource called {{ExamplePlaceIndex}} using {{Esri}} as the data provider.

```
aws location \
  create-place-index \
  --data-source "{{Esri}}" \
  --description "Example place index" \
  --index-name "{{ExamplePlaceIndex}}" \
  --tags Tag1=Value1
```

------

**Note**
Billing depends on your usage. You may incur fees for the use of other AWS services. For more information, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/).

## Authenticating your requests
<a name="places-identity-pool"></a>

Once you create a place index resource and you're ready to begin building location features into your application, choose how you would authenticate your requests:
+ To explore ways you can access the services, see [Accessing Amazon Location Service](how-to-access.md).
+ If you have a website with anonymous users, you may want to use API Keys or Amazon Cognito.

  **Example**

  The following example shows using an API key for authorization, using [AWS JavaScript SDK v3](https://aws.amazon.com/sdk-for-javascript/), and the Amazon Location [JavaScript Authentication helper](loc-sdk-auth.md).

  ```
  import { LocationClient, SearchPlaceIndexForTextCommand } from "@aws-sdk/client-location";
  import { withAPIKey } from "@aws/amazon-location-utilities-auth-helper";

  const apiKey = "{{v1.public.your-api-key-value}}"; // API key

  // Create an authentication helper instance using an API key
  const authHelper = await withAPIKey(apiKey);

  const client = new LocationClient({
    region: "{{<region>}}", // region containing Cognito pool
    ...authHelper.getLocationClientConfig(), // Provides configuration required to make requests to Amazon Location
  });

  const input = {
    IndexName: "{{ExamplePlaceIndex}}",
    Text: "Anyplace",
    BiasPosition: [-123.4567, 45.6789]
  };

  const command = new SearchPlaceIndexForTextCommand(input);

  const response = await client.send(command);
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
