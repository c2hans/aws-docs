---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/validate-emergency-addresses.html
---

# Validating addresses for emergency calls
<a name="validate-emergency-addresses"></a>

To use building addresses for emergency calls, you enter and validate the addresses that the calls can originate from. The Amazon Chime SDK then routes the calls to the nearest local Public Safety Answering Point (PSAP). Remember the following:
+ You only need to validate an address once, but you can validate it multiple times.
+ You only validate a building's address. Don't include suite or apartment numbers.
+ You can only validate addresses in the U.S.

**Note**
We strongly recommend using your validated addresses in PIDF-LO objects in your SIP requests. For more information, see [Using PIDF-LO in emergency calls](use-pidf-lo.md).

**To validate an address**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under `Phone Numbers`, choose `Emergency Calling`.

1.  Under `Validate Address`, enter your building's address.
**Note**
Enter the address exactly as it appears in the SIP Invite. This ensures the address will be recognized when someone calls.

1. Choose `Validate`.
