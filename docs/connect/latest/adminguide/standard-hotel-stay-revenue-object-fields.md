---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/standard-hotel-stay-revenue-object-fields.html
---

# Customer Profiles standard hotel stay revenue object fields
<a name="standard-hotel-stay-revenue-object-fields"></a>

The following table lists all the fields in the Customer Profiles standard hotel stay revenue object.

**Hotel Stay Revenue**

| Standard hotelStayRevenue field | Type | Description |
| --- | --- | --- |
| StayRevenueId | String | The unique identifier of the standard hotel stay revenue. |
| CurrencyCode | String | ISO code for the currency (for example, USD) |
| CurrencyName | String | Full name of the currency (for example, US Dollar) |
| CurrencySymbol | String | Symbol of the currency (for example, $) |
| ReservationId | String | Unique identifier for the hotel reservation |
| GuestId | String | Unique identifier for the guest |
| LastUpdatedOn | String | Timestamp of the last update to the stay record |
| CreatedOn | String | Timestamp of when the stay record was created |
| LastUpdatedBy | String | Identifier of the user/system that last updated the stay record |
| CreatedBy | String | Identifier of the user/system that created the stay record |
| StartDate | String | Start date of the hotel stay |
| HotelCode | String | Code identifying the specific hotel |
| Type | String | Type of revenue (for example, room rate, incidentals, taxes) |
| Description | String | Description of the revenue item |
| Amount | String | Amount of the revenue item |
| ProcessedDate | String | Date the revenue was processed |
| Status | String | Status of the revenue item |
| Attributes | Map<String, String> | Additional metadata or program-specific values. |

**Standard Index Fields**

| Standard index name | Standard preference record field |
| --- | --- |
| \_hotelStayRevenueId | StayRevenueId |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
