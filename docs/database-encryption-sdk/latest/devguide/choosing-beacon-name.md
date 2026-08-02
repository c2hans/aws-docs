---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/choosing-beacon-name.html
---

# Choosing a beacon name
<a name="choosing-beacon-name"></a>

****

|  |
| --- |
| Our client-side encryption library was renamed to the AWS Database Encryption SDK. This developer guide still provides information on the [DynamoDB Encryption Client](legacy-dynamodb-encryption-client.md). |

Every beacon is identified by a unique *beacon name*. Once a beacon is configured, the beacon name is the name you use when querying an encrypted field. A beacon name can be the same name as an encrypted field or [virtual field](beacons.md#virtual-field), but it cannot be the same name as an unencrypted field. Two different beacons cannot have the same beacon name.

For examples demonstrating how to name and configure beacons, see [Configuring beacons](configure-beacons.md).

**Naming standard beacon**
When naming standard beacons, we strongly recommend that your beacon name resolves to the [*beacon source*](beacons.md#beacon-source) whenever possible. This means that the beacon name and the name of the encrypted or [virtual](beacons.md#virtual-field) field that your standard beacon is constructed from are the same. For example, if you are creating a standard beacon for an encrypted field named `LastName`, your beacon name should also be `LastName`.

When your beacon name is the same as the beacon source, you can omit the beacon source from your configuration and the AWS Database Encryption SDK will automatically use the beacon name as the beacon source.
