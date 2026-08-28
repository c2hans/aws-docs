---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-geofence.html
---

# Tutorial: Create a Geofence Collection
<a name="qs-android-tracking-geofence"></a>

Now will you create a geofence collection. You can use either the console, API or CLI. The following procedures walk you through each option.
+ Create a geofence collection using the Amazon Location console:

  1.  Open the [Geofence Collections](https://console.aws.amazon.com/location/geofencing/home#/) section of the Amazon Location console.

  1. Choose **Create geofence collection**.

  1. Provide a name and description for the collection.

  1. Under the EventBridge rule with Amazon CloudWatch as a target, you can create an optional EventBridge rule to get started reacting to geofence events. This enables Amazon Location to publish events to Amazon CloudWatch Logs.

  1. Press the **Create geofence collection** to finish creating the collection.
+ Create a geofence collection using the Amazon Location API:

  Use the [CreateGeofenceCollection](https://docs.aws.amazon.com/location/previous/APIReference/API_CreateGeofenceCollection.html) operation from the Amazon Location Geofences APIs. The following example uses an API request to create a geofence collection called `{{GEOCOLLECTION_NAME}}`.

  ```
  POST /geofencing/v0/collections
  Content-type: application/json

  {
     "CollectionName": "{{GEOCOLLECTION_NAME}}",
     "Description": "Geofence collection 1 for shopping center",
     "Tags": {
        "Tag1" : "Value1"
     }
  }
  ```
+ Create a geofence collection using AWS CLI commands:

  Use the `create-geofence-collection` command. The following example uses an AWS CLI to create a geofence collection called `{{GEOCOLLECTION_NAME}}`. For more information on using the AWS CLI, see the [AWS Command Line Interface Documentation](https://docs.aws.amazon.com/cli/).

  ```
  aws location \
    create-geofence-collection \
    --collection-name "ExampleGeofenceCollection" \
    --description "Shopping center geofence collection" \
    --tags Tag1=Value1
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
