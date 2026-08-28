---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Reservation.html
---

# Reservation
<a name="API_Reservation"></a>

Represents an Amazon Redshift Serverless reservation, which gives you the option to commit to a specified number of Redshift Processing Units (RPUs) for a year at a discount from Serverless on-demand (OD) rates.

## Contents
<a name="API_Reservation_Contents"></a>

 ** capacity **   <a name="redshiftserverless-Type-Reservation-capacity"></a>
The number of Redshift Processing Units (RPUs) to reserve.
Type: Integer
Required: No

 ** endDate **   <a name="redshiftserverless-Type-Reservation-endDate"></a>
The end date for the serverless reservation. This date is one year after the start date that you specify.
Type: Timestamp
Required: No

 ** offering **   <a name="redshiftserverless-Type-Reservation-offering"></a>
The type of offering for the reservation. The offering class determines the payment schedule for the reservation.
Type: [ReservationOffering](API_ReservationOffering.md) object
Required: No

 ** reservationArn **   <a name="redshiftserverless-Type-Reservation-reservationArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the serverless reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** reservationId **   <a name="redshiftserverless-Type-Reservation-reservationId"></a>
The identifier that uniquely identifies the serverless reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** startDate **   <a name="redshiftserverless-Type-Reservation-startDate"></a>
The start date for the serverless reservation. This is the date you created the reservation.
Type: Timestamp
Required: No

 ** status **   <a name="redshiftserverless-Type-Reservation-status"></a>
The status of the reservation. Possible values include the following:
+  `payment-pending`
+  `active`
+  `payment-failed`
+  `retired`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Required: No

## See Also
<a name="API_Reservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Reservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Reservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Reservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
