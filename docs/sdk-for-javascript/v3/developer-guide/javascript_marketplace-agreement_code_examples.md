---
source_url: https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_marketplace-agreement_code_examples.html
---

 The [AWS SDK for JavaScript V3 API Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript version 3 (V3).

# AWS Marketplace Agreement API examples using SDK for JavaScript (v3)

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for JavaScript (v3) with AWS Marketplace Agreement API.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Agreements](#agreements)

## Agreements
<a name="agreements"></a>

### Accept an agreement cancellation request
<a name="marketplace-agreement_AcceptAgreementCancellationRequest_javascript_topic"></a>

The following code example shows how to accept an agreement cancellation request initiated by the seller.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    AcceptAgreementCancellationRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const AGREEMENT_CANCELLATION_REQUEST_ID = "<AGREEMENT CANCELLATION REQUEST ID HERE>";

async function acceptAgreementCancellationRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new AcceptAgreementCancellationRequestCommand({
            agreementId: AGREEMENT_ID,
            agreementCancellationRequestId: AGREEMENT_CANCELLATION_REQUEST_ID,
        })
    );

    console.log("Agreement ID: " + response.agreementId);
    console.log("Cancellation Request ID: " + response.agreementCancellationRequestId);
    console.log("Status: " + response.status);
    console.log("Description: " + response.description);
    console.log("Reason Code: " + response.reasonCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

acceptAgreementCancellationRequest();
```
+  For API details, see [AcceptAgreementCancellationRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/AcceptAgreementCancellationRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Accept an agreement payment request
<a name="marketplace-agreement_AcceptAgreementPaymentRequest_javascript_topic"></a>

The following code example shows how to accept an agreement payment request initiated by the seller.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    AcceptAgreementPaymentRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const PAYMENT_REQUEST_ID = "<PAYMENT REQUEST ID HERE>";
const PURCHASE_ORDER_REFERENCE = "<PURCHASE ORDER REFERENCE HERE>";

async function acceptAgreementPaymentRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new AcceptAgreementPaymentRequestCommand({
            agreementId: AGREEMENT_ID,
            paymentRequestId: PAYMENT_REQUEST_ID,
            purchaseOrderReference: PURCHASE_ORDER_REFERENCE,
        })
    );

    console.log("Payment Request ID: " + response.paymentRequestId);
    console.log("Agreement ID: " + response.agreementId);
    console.log("Status: " + response.status);
    console.log("Name: " + response.name);
    console.log("Charge Amount: " + response.chargeAmount);
    console.log("Currency Code: " + response.currencyCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

acceptAgreementPaymentRequest();
```
+  For API details, see [AcceptAgreementPaymentRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/AcceptAgreementPaymentRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Amend a SaaS contract agreement renewal term
<a name="marketplace-agreement_AmendSaaSContractRenewalTerm_javascript_topic"></a>

The following code example shows how to amend a SaaS contract agreement to add or update its renewal term.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const {
    generateClientToken,
    formatOutput,
    pollUntilEntitlementsAvailable,
    printRenewalTerm,
    printEndTimeBehavior,
} = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create a SaaS agreement with CONTRACT pricing model and then turn on
 * the auto-renewal setting using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer subscribes to a SaaS product using a public offer that supports
 * auto-renewal. After acceptance, the buyer decides to amend the agreement to enable
 * auto-renewal via the RenewalTerm configuration.
 *
 * The lockoutPeriod on the renewal term is what constrains this amendment. It is the renewal
 * decision deadline, measured back from the end date of the agreement, and once it passes neither
 * party can change whether the agreement renews. The sample reads the term with GetAgreementTerms
 * before amending so that deadline is visible. It also reads endTimeBehavior from DescribeAgreement
 * before and after the amendment, because endTimeBehavior is what determines whether the agreement
 * renews, not enableAutoRenew on its own.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offer:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the offer.
 *   - Term IDs (starting with "term-") — found in the offer's term list.
 *   - SELECTOR_VALUE — duration for the agreement (e.g., "P1M" for 1 month).
 *   - DIMENSION_1_KEY — the dimension key defined in the offer.
 */

// The agreementProposalId from the offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the ConfigurableUpfrontPricingTerm in your offer.
const CONFIGURABLE_UPFRONT_PRICING_TERM_ID = "<your-configurable-upfront-pricing-term-id>";

// Duration for the agreement (e.g., "P1M" for 1 month, "P12M" for 1 year).
const SELECTOR_VALUE = "<your-selector-value>";

// The dimension key defined in your offer.
const DIMENSION_1_KEY = "<your-dimension-key>";

// Quantity for the dimension.
const DIMENSION_1_VALUE = 1;

// Term ID for the RenewalTerm in your offer.
const RENEWAL_TERM_ID = "<your-renewal-term-id>";

// Term ID for the LegalTerm in your offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Term ID for the SupportTerm in your offer.
const SUPPORT_TERM_ID = "<your-support-term-id>";

/**
 * Full end-to-end flow:
 * 1. Create a SaaS agreement with CONTRACT pricing model with auto-renewal disabled.
 * 2. Wait for entitlements to become active.
 * 3. Amend the agreement to enable auto-renewal.
 * 4. Confirm the change by reading endTimeBehavior before and after the amendment.
 */
async function amendSaaSContractAgreementRenewalTerm() {
    const client = new MarketplaceAgreementClient();

    const configurableUpfrontPricingTerm = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: DIMENSION_1_VALUE },
                ],
            },
        },
    };

    // Initial agreement: auto-renewal disabled.
    const renewalTerm = {
        id: RENEWAL_TERM_ID,
        configuration: {
            renewalTermConfiguration: {
                enableAutoRenew: false,
            },
        },
    };

    const legalTerm = { id: LEGAL_TERM_ID };
    const supportTerm = { id: SUPPORT_TERM_ID };

    // --- Create and accept the initial SaaS agreement request with CONTRACT pricing model ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [configurableUpfrontPricingTerm, renewalTerm, legalTerm, supportTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement request accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);

    // Wait for entitlements to become active before amending.
    console.log("Waiting for entitlements to become active...");
    const entitlementsResponse = await pollUntilEntitlementsAvailable(client, acceptAgreementRequestResponse.agreementId);
    console.log("Entitlements are now active.");
    formatOutput(entitlementsResponse);

    await printRenewalTerm(client, acceptAgreementRequestResponse.agreementId);
    await printEndTimeBehavior(client, acceptAgreementRequestResponse.agreementId, "Before amendment");

    // --- Amend: enable auto-renewal ---
    // The lockoutPeriod printed above is the renewal decision deadline: once it passes,
    // enableAutoRenew can no longer be changed.
    const renewalTermAmended = {
        id: RENEWAL_TERM_ID,
        configuration: {
            renewalTermConfiguration: {
                enableAutoRenew: true,
            },
        },
    };

    // Use Intent.AMEND and sourceAgreementIdentifier to target the existing agreement.
    const carResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "AMEND",
            requestedTerms: [configurableUpfrontPricingTerm, renewalTermAmended, legalTerm, supportTerm],
            sourceAgreementIdentifier: acceptAgreementRequestResponse.agreementId,
        })
    );
    console.log("Amend agreement request created. AgreementRequestId: " + carResponse.agreementRequestId);

    const aarResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carResponse.agreementRequestId,
        })
    );
    console.log("Amendment accepted. Auto-renewal enabled. New AgreementId: " + aarResponse.agreementId);

    await printEndTimeBehavior(client, aarResponse.agreementId, "After amendment");
}

amendSaaSContractAgreementRenewalTerm();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Amend an AMI ConfigurableUpfrontPricingTerm for usage pricing model
<a name="marketplace-agreement_AmendAmiConfigurableUpfrontPricingTermForUsagePricingModel_javascript_topic"></a>

The following code example shows how to amend an AMI agreement with ConfigurableUpfrontPricingTerm by updating dimension quantity for usage pricing model.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken, formatOutput, pollUntilEntitlementsAvailable } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create an AMI agreement with ConfigurableUpfrontPricingTerm and then amend the dimension quantity
 * using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: An AMI product with USAGE pricing requires two agreements:
 *   1. An agreement with usageBasedPricingTerm (UBPT) — accepted first to establish the base agreement.
 *   2. An agreement with configurableUpfrontPricingTerm (CUPT) — accepted after the UBPT agreement entitlements are active.
 *
 * Once both agreement entitlements are available, this sample shows how to amend the agreement
 * with configurableUpfrontPricingTerm (CUPT) to increase the dimension quantity.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offer:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the offer.
 *   - Term IDs (starting with "term-") — found in the offer's term list.
 *   - SELECTOR_VALUE — duration for the agreement (e.g., "P365D" for one year).
 *   - DIMENSION_1_KEY — the dimension key defined in the offer (e.g., instance type).
 *   - DIMENSION_1_VALUE — initial quantity; NEW_DIMENSION_1_VALUE — amended quantity.
 */

// The agreementProposalId from the offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the ConfigurableUpfrontPricingTerm in your offer.
const CONFIGURABLE_UPFRONT_PRICING_TERM_ID = "<your-configurable-upfront-pricing-term-id>";

// Duration for the agreement (e.g., "P365D" for 365 days).
const SELECTOR_VALUE = "<your-selector-value>";

// The dimension key defined in your offer (e.g., an EC2 instance type like "c6gn.medium").
const DIMENSION_1_KEY = "<your-dimension-key>";

// Initial quantity for the dimension.
const DIMENSION_1_VALUE = 1;

// Term ID for the UsageBasedPricingTerm in your offer.
const USAGE_TERM_ID = "<your-usage-term-id>";

// Term ID for the LegalTerm in your offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Term ID for the ValidityTerm in your offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

// New quantity to use when amending the dimension of CUPT.
const NEW_DIMENSION_1_VALUE = 5;

/**
 * Full end-to-end flow:
 * 1. Create and accept an agreement request with usageBasedPricingTerm.
 * 2. Wait for entitlements to become active, then create and accept an agreement request with configurableUpfrontPricingTerm (CUPT).
 * 3. Wait for CUPT entitlements to become active, then amend the dimension quantity.
 */
async function amendAmiCUPTAgreement() {
    const client = new MarketplaceAgreementClient();

    const usageTerm = { id: USAGE_TERM_ID };
    const legalTerm = { id: LEGAL_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };

    // --- Agreement with UBPT ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [usageTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with UBPT created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement request with UBPT accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);

    // Wait for entitlements to become active before creating the agreement with CUPT.
    console.log("Waiting for UBPT agreement entitlements to become active...");
    const entitlementsResponse = await pollUntilEntitlementsAvailable(client, acceptAgreementRequestResponse.agreementId);
    console.log("UBPT agreement entitlements are now active.");
    formatOutput(entitlementsResponse);

    // --- Agreement with configurableUpfrontPricingTerm (CUPT) ---
    const configurableUpfrontPricingTerm = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: DIMENSION_1_VALUE },
                ],
            },
        },
    };

    const carResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [configurableUpfrontPricingTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with CUPT created. AgreementRequestId: " + carResponse.agreementRequestId);

    const aarResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carResponse.agreementRequestId,
        })
    );
    const cuptAgreementId = aarResponse.agreementId;
    console.log("Agreement request with CUPT accepted. AgreementId: " + cuptAgreementId);

    // Wait for entitlements to become active before amending.
    console.log("Waiting for CUPT agreement entitlements to become active...");
    const cuptEntitlementsResponse = await pollUntilEntitlementsAvailable(client, cuptAgreementId);
    console.log("CUPT agreement entitlements are now active.");
    formatOutput(cuptEntitlementsResponse);

    // --- Amend Agreement with CUPT ---
    // Increase the dimension quantity using Intent.AMEND and sourceAgreementIdentifier.
    const newConfig = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: NEW_DIMENSION_1_VALUE }, // Increase quantity for this dimension key
                ],
            },
        },
    };

    const carAmendResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "AMEND",
            requestedTerms: [newConfig, legalTerm, validityTerm],
            sourceAgreementIdentifier: cuptAgreementId,
        })
    );
    console.log("Amendment of CUPT agreement request created. AgreementRequestId: " + carAmendResponse.agreementRequestId);

    const aarAmendResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carAmendResponse.agreementRequestId,
        })
    );
    console.log("Amendment accepted. New AgreementId: " + aarAmendResponse.agreementId);
}

amendAmiCUPTAgreement();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Approve an agreement approval
<a name="marketplace-agreement_AcceptAgreementApproval_javascript_topic"></a>

The following code example shows how to approve an agreement approval as the administrator of my organization.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    AcceptAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Approves an agreement approval as the administrator of the buyer's AWS Organization. When the approval
// is approved, the agreement request is accepted and the agreement is created; GetAgreementRequest returns its
// agreementId.
const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
const NOTE = "<APPROVAL NOTE HERE>";

async function acceptAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new AcceptAgreementApprovalCommand({
            buyerAgreementApprovalApproverInput: {
                agreementApprovalId: AGREEMENT_APPROVAL_ID,
                note: NOTE,
            },
        })
    );

    console.log("Approved Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
}

acceptAgreementApproval();
```
+  For API details, see [AcceptAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/AcceptAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*.

### Cancel an agreement request
<a name="marketplace-agreement_CancelAgreementRequest_javascript_topic"></a>

The following code example shows how to cancel an agreement request that is pending approval.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CancelAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Cancels an agreement request that is pending approval, and its approval.
const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function cancelAgreementRequest() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new CancelAgreementRequestCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
        })
    );

    console.log("Cancelled Agreement Request ID: " + AGREEMENT_REQUEST_ID);
}

cancelAgreementRequest();
```
+  For API details, see [CancelAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CancelAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Create a new AMI free trial agreement
<a name="marketplace-agreement_NewAmiFreeTrial_javascript_topic"></a>

The following code example shows how to create a new AMI free trial agreement.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create an AMI Free Trial agreement
 * using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer subscribes to an AMI product that offers a free trial period.
 * The free trial includes a FreeTrialPricingTerm alongside a UsageBasedPricingTerm.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offer:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the offer.
 *   - Term IDs (starting with "term-") — found in the offer's term list.
 */

// The agreementProposalId from the offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the FreeTrialPricingTerm in your offer.
const FREE_TRIAL_PRICING_TERM_ID = "<your-free-trial-pricing-term-id>";

// Term ID for the UsageBasedPricingTerm in your offer (applies after the trial ends).
const USAGE_BASED_PRICING_TERM_ID = "<your-usage-based-pricing-term-id>";

// Term ID for the SupportTerm in your offer.
const SUPPORT_TERM_ID = "<your-support-term-id>";

// Term ID for the LegalTerm in your offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

/**
 * Creates an AMI Free Trial agreement.
 * The FreeTrialPricingTerm grants access at no cost for the trial period.
 * The UsageBasedPricingTerm defines the charges that apply once the trial ends.
 */
async function createAndAcceptAmiFreeTrialAgreementRequest() {
    const client = new MarketplaceAgreementClient();

    const freeTrialPricingTerm = { id: FREE_TRIAL_PRICING_TERM_ID };
    const usageBasedPricingTerm = { id: USAGE_BASED_PRICING_TERM_ID };
    const supportTerm = { id: SUPPORT_TERM_ID };
    const legalTerm = { id: LEGAL_TERM_ID };

    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [freeTrialPricingTerm, usageBasedPricingTerm, supportTerm, legalTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement request with freeTrialPricingTerm accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);
}

createAndAcceptAmiFreeTrialAgreementRequest();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Create a new SaaS contract agreement with upfront payment
<a name="marketplace-agreement_NewSaaSContractWithUpfrontPayment_javascript_topic"></a>

The following code example shows how to create a new SaaS contract agreement with upfront payment.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create a SaaS agreement with CONTRACT pricing model with upfront payment
 * using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer subscribes to a SaaS product using a ConfigurableUpfrontPricingTerm,
 * selecting an agreement duration and specifying quantities for multiple dimensions.
 * Tax estimation is enabled at the time of agreement creation.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offer:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the offer.
 *   - Term IDs (starting with "term-") — found in the offer's term list.
 *   - SELECTOR_VALUE — duration for the agreement (e.g., "P12M" for 12 months).
 *   - DIMENSION_1_KEY, DIMENSION_2_KEY — dimension keys defined in the offer.
 *   - DIMENSION_1_VALUE, DIMENSION_2_VALUE — quantities for each dimension.
 */

// The agreementProposalId from the offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the ConfigurableUpfrontPricingTerm in your offer.
const CONFIGURABLE_UPFRONT_PRICING_TERM_ID = "<your-configurable-upfront-pricing-term-id>";

// Duration for the agreement (e.g., "P12M" for 12 months).
const SELECTOR_VALUE = "<your-selector-value>";

// First dimension key and quantity defined in your offer.
const DIMENSION_1_KEY = "<your-dimension-1-key>";
const DIMENSION_1_VALUE = 10;

// Second dimension key and quantity defined in your offer.
const DIMENSION_2_KEY = "<your-dimension-2-key>";
const DIMENSION_2_VALUE = 20;

// Term ID for the LegalTerm in your offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Tax estimation setting: "ENABLED" to include estimated taxes in the agreement.
const TAX_ESTIMATION = "ENABLED";

/**
 * Creates a SaaS agreement with CONTRACT pricing model with configurable upfront pricing
 * for multiple dimensions and tax estimation.
 */
async function createSaaSContractAgreement() {
    const client = new MarketplaceAgreementClient();

    const configurableUpfrontPricingTerm = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: DIMENSION_1_VALUE },
                    { dimensionKey: DIMENSION_2_KEY, dimensionValue: DIMENSION_2_VALUE },
                ],
            },
        },
    };

    const legalTerm = { id: LEGAL_TERM_ID };

    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [configurableUpfrontPricingTerm, legalTerm],
            taxConfiguration: { taxEstimation: TAX_ESTIMATION },
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("SaaS agreement request with CONTRACT pricing model accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);
}

createSaaSContractAgreement();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Get details of an agreement approval
<a name="marketplace-agreement_GetAgreementApproval_javascript_topic"></a>

The following code example shows how to get details of an agreement approval, including its approver outcomes.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";

async function getAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementApprovalCommand({
            agreementApprovalId: AGREEMENT_APPROVAL_ID,
        })
    );
    const approval = response.buyerAgreementApproval;

    console.log("Approval Type: " + approval.approvalType);
    console.log("Agreement Approval ID: " + approval.agreementApprovalId);
    console.log("Agreement Request ID: " + approval.agreementRequestId);
    console.log("Name: " + approval.name);
    console.log("Status: " + approval.status);
    console.log("Requester Account ID: " + approval.requester.accountId);
    console.log("Proposer: " + approval.proposer.legalName + " (" + approval.proposer.accountId + ")");
    console.log("Offer ID: " + approval.proposalSummary.offerId);
    if (approval.proposalSummary.offerSetId !== undefined) {
        console.log("Offer Set ID: " + approval.proposalSummary.offerSetId);
    }
    console.log("Visibility Scope: " + approval.proposalSummary.visibilityScope);
    for (const resource of approval.proposalSummary.resources ?? []) {
        console.log("Resource: " + resource.name + " (" + resource.id + ", " + resource.type + ")");
    }
    console.log("Plan Reference: " + approval.planInput.planReference);
    if (approval.planInput.requesterNote !== undefined) {
        console.log("Requester Note: " + approval.planInput.requesterNote);
    }
    console.log("Created At: " + approval.createdAt);
    console.log("Updated At: " + approval.updatedAt);
    console.log("Started At: " + approval.startedAt);
    console.log("Expires At: " + approval.expiresAt);
    console.log("Approval Needed By: " + approval.approvalNeededBy);
    for (const level of approval.levels) {
        console.log("  Level: " + level.name);
        for (const group of level.groups) {
            console.log("    Required Approvals: " + group.approvalCriteria.requiredApprovalCount);
            for (const outcome of group.approvers) {
                printApproverOutcome(outcome);
            }
        }
    }
}

function printApproverOutcome(outcome) {
    if (outcome.awsOrganizationApproverOutcome) {
        const admin = outcome.awsOrganizationApproverOutcome;
        console.log("    Organization admin: " + admin.status + ", approverOutcomeId " + admin.approverOutcomeId);
    } else if (outcome.emailApproverOutcome) {
        const email = outcome.emailApproverOutcome;
        console.log("    Email approver " + email.emailAddress + ": " + email.status
            + ", approverOutcomeId " + email.approverOutcomeId);
    } else if (outcome.procurementToolApproverOutcome) {
        const tool = outcome.procurementToolApproverOutcome;
        console.log("    Procurement tool " + tool.name + ": " + tool.status
            + ", approverOutcomeId " + tool.approverOutcomeId);
    } else {
        console.log("    Approver: " + JSON.stringify(outcome));
    }
}

getAgreementApproval();
```
+  For API details, see [GetAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*.

### Get details of an agreement cancellation request
<a name="marketplace-agreement_GetAgreementCancellationRequest_javascript_topic"></a>

The following code example shows how to get details of a specific agreement cancellation request.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementCancellationRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const AGREEMENT_CANCELLATION_REQUEST_ID = "<AGREEMENT CANCELLATION REQUEST ID HERE>";

async function getAgreementCancellationRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementCancellationRequestCommand({
            agreementId: AGREEMENT_ID,
            agreementCancellationRequestId: AGREEMENT_CANCELLATION_REQUEST_ID,
        })
    );

    console.log("Agreement ID: " + response.agreementId);
    console.log("Cancellation Request ID: " + response.agreementCancellationRequestId);
    console.log("Status: " + response.status);
    console.log("Status Message: " + response.statusMessage);
    console.log("Reason Code: " + response.reasonCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

getAgreementCancellationRequest();
```
+  For API details, see [GetAgreementCancellationRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementCancellationRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Get details of an agreement payment request
<a name="marketplace-agreement_GetAgreementPaymentRequest_javascript_topic"></a>

The following code example shows how to get details of a specific agreement payment request.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementPaymentRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const PAYMENT_REQUEST_ID = "<PAYMENT REQUEST ID HERE>";

async function getAgreementPaymentRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementPaymentRequestCommand({
            agreementId: AGREEMENT_ID,
            paymentRequestId: PAYMENT_REQUEST_ID,
        })
    );

    console.log("Payment Request ID: " + response.paymentRequestId);
    console.log("Agreement ID: " + response.agreementId);
    console.log("Status: " + response.status);
    console.log("Status Message: " + response.statusMessage);
    console.log("Name: " + response.name);
    console.log("Charge ID: " + response.chargeId);
    console.log("Charge Amount: " + response.chargeAmount);
    console.log("Currency Code: " + response.currencyCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

getAgreementPaymentRequest();
```
+  For API details, see [GetAgreementPaymentRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementPaymentRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Get details of an agreement request
<a name="marketplace-agreement_GetAgreementRequest_javascript_topic"></a>

The following code example shows how to get details of an agreement request, including whether it requires approval and its expected charges.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    GetAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new GetAgreementRequestCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
        })
    );

    console.log("Agreement Request ID: " + response.agreementRequestId);
    console.log("Agreement Type: " + response.agreementType);
    console.log("Status: " + response.status);
    console.log("Approval Requirement: " + response.approvalRequirement);
    if (response.agreementId !== undefined) {
        console.log("Agreement ID: " + response.agreementId);
    }
    console.log("Intent: " + response.intent);
    console.log("Created At: " + response.createdAt);

    const chargeSummary = response.chargeSummary;
    console.log("Currency Code: " + chargeSummary.currencyCode);
    console.log("New Agreement Value: " + chargeSummary.newAgreementValue);
    // Tax fields are returned only when the request was created with tax estimation enabled.
    if (chargeSummary.estimatedTaxes !== undefined) {
        console.log("New Agreement Value After Tax: " + chargeSummary.newAgreementValueAfterTax);
        console.log("Estimated Taxes: " + chargeSummary.estimatedTaxes.totalAmount);
        console.log("Invoicing Entity: " + JSON.stringify(chargeSummary.invoicingEntity));
    }
    for (const charge of chargeSummary.expectedCharges ?? []) {
        console.log("Expected Charge ID: " + charge.id);
        console.log("  Amount: " + charge.amount);
        if (charge.amountAfterTax !== undefined) {
            console.log("  Amount After Tax: " + charge.amountAfterTax);
        }
        console.log("  Timing: " + charge.timing);
        // Recurring charges of usage-based and recurring payment terms have no time.
        if (charge.time !== undefined) {
            console.log("  Time: " + charge.time);
        }
        if (charge.purchaseOrderReference !== undefined) {
            console.log("  Purchase Order Reference: " + charge.purchaseOrderReference);
        }
    }
    for (const itemizedCharge of chargeSummary.itemizedCharges ?? []) {
        console.log("Itemized Charge: " + itemizedCharge.dimensionKey + ", quantity "
            + itemizedCharge.oldQuantity + " -> " + itemizedCharge.newQuantity + ", amount "
            + itemizedCharge.incrementalChargeAmount);
    }

    console.log("Proposer Account ID: " + response.proposer.accountId);
    console.log("Offer ID: " + response.proposalSummary.offerId);
    if (response.proposalSummary.offerSetId !== undefined) {
        console.log("Offer Set ID: " + response.proposalSummary.offerSetId);
    }
    for (const resource of response.proposalSummary.resources ?? []) {
        console.log("Resource: " + resource.id + " (" + resource.type + ")");
    }
}

getAgreementRequest();
```
+  For API details, see [GetAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Get the approval plans of an agreement request
<a name="marketplace-agreement_GetAgreementRequestApprovalPlans_javascript_topic"></a>

The following code example shows how to get the approval plans that apply to an agreement request.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    paginateGetAgreementRequestApprovalPlans,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequestApprovalPlans() {
    const client = new MarketplaceAgreementClient();

    for await (const page of paginateGetAgreementRequestApprovalPlans(
        { client },
        { agreementRequestId: AGREEMENT_REQUEST_ID }
    )) {
        for (const item of page.items) {
            const plan = item.buyerAgreementApprovalPlan;
            console.log("Plan Reference: " + plan.planReference);
            console.log("Plan Name: " + plan.name);
            for (const level of plan.levels) {
                console.log("  Level: " + level.name);
                for (const group of level.groups) {
                    console.log("    Required Approvals: " + group.approvalCriteria.requiredApprovalCount);
                    for (const approver of group.approvers) {
                        console.log("    Approver: " + JSON.stringify(approver));
                    }
                }
            }
            console.log("---");
        }
    }
}

getAgreementRequestApprovalPlans();
```
+  For API details, see [GetAgreementRequestApprovalPlans](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestApprovalPlansCommand) in *AWS SDK for JavaScript API Reference*.

### Get the terms of an agreement request
<a name="marketplace-agreement_GetAgreementRequestTerms_javascript_topic"></a>

The following code example shows how to get the terms requested in an agreement request.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    paginateGetAgreementRequestTerms,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";

async function getAgreementRequestTerms() {
    const client = new MarketplaceAgreementClient();

    for await (const page of paginateGetAgreementRequestTerms(
        { client },
        { agreementRequestId: AGREEMENT_REQUEST_ID }
    )) {
        for (const term of page.terms) {
            const [termType, termValue] = Object.entries(term)[0];
            console.log("Term Type: " + termType);
            console.log(JSON.stringify(termValue, null, 2));
            console.log("---");
        }
    }
}

getAgreementRequestTerms();
```
+  For API details, see [GetAgreementRequestTerms](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/GetAgreementRequestTermsCommand) in *AWS SDK for JavaScript API Reference*.

### List agreement approvals
<a name="marketplace-agreement_ListAgreementApprovals_javascript_topic"></a>

The following code example shows how to list the agreement approvals I requested, or that I decide as the administrator of my organization.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementApprovalsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// REQUESTER lists the approvals the caller started. AWS_ORGANIZATION_ADMIN lists the approvals the caller
// decides as the administrator of its AWS Organization.
const PARTY_TYPE = "AWS_ORGANIZATION_ADMIN";
const STATUS = "PENDING_APPROVAL";

async function listAgreementApprovals() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementApprovalsCommand({
                partyType: PARTY_TYPE,
                status: STATUS,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items) {
            console.log("Approval Type: " + summary.approvalType);
            console.log("Agreement Request ID: " + summary.agreementRequestId);
            console.log("Agreement Approval ID: " + summary.agreementApprovalId);
            console.log("Name: " + summary.name);
            console.log("Status: " + summary.status);
            console.log("Created At: " + summary.createdAt);
            console.log("Updated At: " + summary.updatedAt);
            console.log("Started At: " + summary.startedAt);
            console.log("Expires At: " + summary.expiresAt);
            console.log("Approval Needed By: " + summary.approvalNeededBy);
            console.log("---");
        }

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementApprovals();
```
+  For API details, see [ListAgreementApprovals](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementApprovalsCommand) in *AWS SDK for JavaScript API Reference*.

### List agreement cancellation requests
<a name="marketplace-agreement_ListAgreementCancellationRequests_javascript_topic"></a>

The following code example shows how to list agreement cancellation requests for agreements I participate in as acceptor.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementCancellationRequestsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const PARTY_TYPE = "Proposer";

async function listAgreementCancellationRequests() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementCancellationRequestsCommand({
                partyType: PARTY_TYPE,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items) {
            console.log("Cancellation Request ID: " + summary.agreementCancellationRequestId);
            console.log("Agreement ID: " + summary.agreementId);
            console.log("Status: " + summary.status);
            console.log("Reason Code: " + summary.reasonCode);
            console.log("Agreement Type: " + summary.agreementType);
            console.log("Catalog: " + summary.catalog);
            console.log("Created At: " + summary.createdAt);
            console.log("Updated At: " + summary.updatedAt);
            console.log("---");
        }

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementCancellationRequests();
```
+  For API details, see [ListAgreementCancellationRequests](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementCancellationRequestsCommand) in *AWS SDK for JavaScript API Reference*.

### List agreement payment requests
<a name="marketplace-agreement_ListAgreementPaymentRequests_javascript_topic"></a>

The following code example shows how to list agreement payment requests for agreements I participate in as acceptor.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementPaymentRequestsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const PARTY_TYPE = "Proposer";

async function listAgreementPaymentRequests() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementPaymentRequestsCommand({
                partyType: PARTY_TYPE,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items) {
            console.log("Payment Request ID: " + summary.paymentRequestId);
            console.log("Agreement ID: " + summary.agreementId);
            console.log("Status: " + summary.status);
            console.log("Name: " + summary.name);
            console.log("Charge ID: " + summary.chargeId);
            console.log("Charge Amount: " + summary.chargeAmount);
            console.log("Currency Code: " + summary.currencyCode);
            console.log("Created At: " + summary.createdAt);
            console.log("Updated At: " + summary.updatedAt);
            console.log("---");
        }

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementPaymentRequests();
```
+  For API details, see [ListAgreementPaymentRequests](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementPaymentRequestsCommand) in *AWS SDK for JavaScript API Reference*.

### List agreement requests
<a name="marketplace-agreement_ListAgreementRequests_javascript_topic"></a>

The following code example shows how to list my agreement requests, filtered by status.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    ListAgreementRequestsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const STATUS = "PENDING_APPROVAL";

async function listAgreementRequests() {
    const client = new MarketplaceAgreementClient();

    let nextToken = null;

    do {
        const response = await client.send(
            new ListAgreementRequestsCommand({
                status: STATUS,
                nextToken: nextToken,
            })
        );

        for (const summary of response.items ?? []) {
            console.log("Agreement Request ID: " + summary.agreementRequestId);
            console.log("Agreement Type: " + summary.agreementType);
            console.log("Status: " + summary.status);
            if (summary.agreementId) {
                console.log("Agreement ID: " + summary.agreementId);
            }
            console.log("Offer ID: " + summary.proposalSummary.offerId);
            if (summary.proposalSummary.offerSetId !== undefined) {
                console.log("Offer Set ID: " + summary.proposalSummary.offerSetId);
            }
            for (const resource of summary.proposalSummary.resources ?? []) {
                console.log("Resource: " + resource.id + " (" + resource.type + ")");
            }
            console.log("---");
        }

        nextToken = response.nextToken;
    } while (nextToken != null);
}

listAgreementRequests();
```
+  For API details, see [ListAgreementRequests](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/ListAgreementRequestsCommand) in *AWS SDK for JavaScript API Reference*.

### Reject an agreement approval
<a name="marketplace-agreement_RejectAgreementApproval_javascript_topic"></a>

The following code example shows how to reject an agreement approval as the administrator of my organization.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    RejectAgreementApprovalCommand,
} = require("@aws-sdk/client-marketplace-agreement");

// Rejects an agreement approval as the administrator of the buyer's AWS Organization. The agreement request
// is rejected and no agreement is created.
const AGREEMENT_APPROVAL_ID = "<AGREEMENT APPROVAL ID HERE>";
const NOTE = "<REJECTION REASON HERE>";

async function rejectAgreementApproval() {
    const client = new MarketplaceAgreementClient();

    await client.send(
        new RejectAgreementApprovalCommand({
            buyerAgreementApprovalRejectionInput: {
                agreementApprovalId: AGREEMENT_APPROVAL_ID,
                note: NOTE,
            },
        })
    );

    console.log("Rejected Agreement Approval ID: " + AGREEMENT_APPROVAL_ID);
}

rejectAgreementApproval();
```
+  For API details, see [RejectAgreementApproval](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/RejectAgreementApprovalCommand) in *AWS SDK for JavaScript API Reference*.

### Reject an agreement cancellation request
<a name="marketplace-agreement_RejectAgreementCancellationRequest_javascript_topic"></a>

The following code example shows how to reject an agreement cancellation request initiated by the seller.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    RejectAgreementCancellationRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const AGREEMENT_CANCELLATION_REQUEST_ID = "<AGREEMENT CANCELLATION REQUEST ID HERE>";
const REJECTION_REASON = "<REJECTION REASON HERE>";

async function rejectAgreementCancellationRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new RejectAgreementCancellationRequestCommand({
            agreementId: AGREEMENT_ID,
            agreementCancellationRequestId: AGREEMENT_CANCELLATION_REQUEST_ID,
            rejectionReason: REJECTION_REASON,
        })
    );

    console.log("Agreement ID: " + response.agreementId);
    console.log("Cancellation Request ID: " + response.agreementCancellationRequestId);
    console.log("Status: " + response.status);
    console.log("Status Message: " + response.statusMessage);
    console.log("Reason Code: " + response.reasonCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

rejectAgreementCancellationRequest();
```
+  For API details, see [RejectAgreementCancellationRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/RejectAgreementCancellationRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Reject an agreement payment request
<a name="marketplace-agreement_RejectAgreementPaymentRequest_javascript_topic"></a>

The following code example shows how to reject an agreement payment request initiated by the seller.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    RejectAgreementPaymentRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_ID = "<AGREEMENT ID HERE>";
const PAYMENT_REQUEST_ID = "<PAYMENT REQUEST ID HERE>";
const REJECTION_REASON = "<REJECTION REASON HERE>";

async function rejectAgreementPaymentRequest() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new RejectAgreementPaymentRequestCommand({
            agreementId: AGREEMENT_ID,
            paymentRequestId: PAYMENT_REQUEST_ID,
            rejectionReason: REJECTION_REASON,
        })
    );

    console.log("Payment Request ID: " + response.paymentRequestId);
    console.log("Agreement ID: " + response.agreementId);
    console.log("Status: " + response.status);
    console.log("Status Message: " + response.statusMessage);
    console.log("Name: " + response.name);
    console.log("Charge Amount: " + response.chargeAmount);
    console.log("Currency Code: " + response.currencyCode);
    console.log("Created At: " + response.createdAt);
    console.log("Updated At: " + response.updatedAt);
}

rejectAgreementPaymentRequest();
```
+  For API details, see [RejectAgreementPaymentRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/RejectAgreementPaymentRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Replace a SaaS contract agreement with an agreement-based offer
<a name="marketplace-agreement_ReplaceSaaSContractWithAgreementBasedOffer_javascript_topic"></a>

The following code example shows how to replace a SaaS contract agreement with a new agreement-based offer.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to replace an existing SaaS agreement with CONTRACT pricing model with a new
 * Agreement-Based Offer (ABO) using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer has an active SaaS agreement with CONTRACT pricing model and receives a private
 * Agreement-Based Offer from the seller. The buyer replaces the existing agreement
 * with the new ABO offer, which may include updated pricing terms and payment schedule.
 *
 * Note: Unlike other Replace samples, this example starts from an already-active
 * EXISTING_AGREEMENT_ID rather than creating a new agreement first. Use this
 * pattern when you already have an agreement ID and want to replace it directly.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offers:
 *   - EXISTING_AGREEMENT_ID — the agreement ID of the active agreement to replace (starts with "agmt-").
 *   - NEW_AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the new ABO offer.
 *   - Term IDs (starting with "term-") — found in the new offer's term list.
 */

// The agreement ID of the active SaaS agreement with CONTRACT pricing model to replace (starts with "agmt-").
const EXISTING_AGREEMENT_ID = "<your-existing-agreement-id>";

// The agreementProposalId from the new Agreement-Based Offer.
const NEW_AGREEMENT_PROPOSAL_IDENTIFIER = "<your-new-agreement-proposal-identifier>";

// Term ID for the LegalTerm in the new offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Term ID for the ValidityTerm in the new offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

// Term ID for the FixedUpfrontPricingTerm in the new offer.
const FIXED_UPFRONT_PRICING_TERM_ID = "<your-fixed-upfront-pricing-term-id>";

// Term ID for the PaymentScheduleTerm in the new offer.
const PAYMENT_SCHEDULE_TERM_ID = "<your-payment-schedule-term-id>";

/**
 * Replaces an existing SaaS agreement with CONTRACT pricing model with a new Agreement-Based Offer.
 * Uses Intent.REPLACE with sourceAgreementIdentifier set to the existing agreement ID.
 */
async function replaceExistingAgreement() {
    const client = new MarketplaceAgreementClient();

    const legalTerm = { id: LEGAL_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };
    const fixedUpfrontPricingTerm = { id: FIXED_UPFRONT_PRICING_TERM_ID };
    const paymentScheduleTerm = { id: PAYMENT_SCHEDULE_TERM_ID };

    // Replace the agreement with the new offer
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "REPLACE",
            requestedTerms: [fixedUpfrontPricingTerm, paymentScheduleTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: NEW_AGREEMENT_PROPOSAL_IDENTIFIER,
            sourceAgreementIdentifier: EXISTING_AGREEMENT_ID,
        })
    );
    console.log("Replace agreement request created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement replaced with ABO. New AgreementId: " + acceptAgreementRequestResponse.agreementId);
}

replaceExistingAgreement();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Replace a SaaS free trial with Contract with Consumption Pricing
<a name="marketplace-agreement_ReplaceSaaSFreeTrialWithCCP_javascript_topic"></a>

The following code example shows how to replace a SaaS free trial with a Contract with Consumption Pricing (CCP).

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken, formatOutput, pollUntilEntitlementsAvailable } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create a SaaS free trial agreement and then replace it with a
 * paid Contract with Consumption Pricing (CCP) offer using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer first starts a free trial on a SaaS product. Once the trial is active,
 * they decide to convert by replacing it with a paid offer that includes a
 * FixedUpfrontPricingTerm, PaymentScheduleTerm, and UsageBasedPricingTerm.
 *
 * Flow:
 *   1. Create a SaaS free trial agreement with freeTrialPricingTerm.
 *   2. Wait for freeTrialPricingTerm agreement entitlements to become active.
 *   3. Replace the free trial agreement with the paid CCP offer using Intent.REPLACE.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offers:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the free trial offer.
 *   - NEW_AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the paid CCP offer.
 *   - Term IDs (starting with "term-") — found in each offer's term list.
 */

// The agreementProposalId from the free trial offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-free-trial-agreement-proposal-identifier>";

// Term ID for the FreeTrialPricingTerm in the free trial offer.
const FREE_TRIAL_PRICING_TERM_ID = "<your-free-trial-pricing-term-id>";

// Term ID for the LegalTerm in the free trial offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// The agreementProposalId from the paid CCP offer to convert to.
const NEW_AGREEMENT_PROPOSAL_IDENTIFIER = "<your-ccp-agreement-proposal-identifier>";

// Term ID for the FixedUpfrontPricingTerm in the CCP offer.
const FIXED_UPFRONT_PRICING_TERM_ID = "<your-fixed-upfront-pricing-term-id>";

// Term ID for the PaymentScheduleTerm in the CCP offer.
const PAYMENT_SCHEDULE_TERM_ID = "<your-payment-schedule-term-id>";

// Term ID for the UsageBasedPricingTerm in the CCP offer.
const USAGE_BASED_PRICING_TERM_ID = "<your-usage-based-pricing-term-id>";

// Term ID for the ValidityTerm in the CCP offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

// Term ID for the LegalTerm in the CCP offer.
const NEW_LEGAL_TERM_ID = "<your-new-legal-term-id>";

/**
 * Full end-to-end flow:
 * 1. Create a SaaS free trial agreement with freeTrialPricingTerm.
 * 2. Wait for freeTrialPricingTerm agreement entitlements to become active.
 * 3. Replace the free trial agreement with the paid CCP offer.
 */
async function createSaaSFreeTrialAndReplaceWithCCP() {
    const client = new MarketplaceAgreementClient();

    const legalTerm = { id: LEGAL_TERM_ID };
    const freeTrialPricingTerm = { id: FREE_TRIAL_PRICING_TERM_ID };

    // --- Step 1: Agreement with freeTrialPricingTerm ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [freeTrialPricingTerm, legalTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with freeTrialPricingTerm created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement request with freeTrialPricingTerm accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);

    // Wait for freeTrialPricingTerm agreement entitlements to become active before replacing.
    console.log("Waiting for freeTrialPricingTerm agreement entitlements to become active...");
    const entitlementsResponse = await pollUntilEntitlementsAvailable(client, acceptAgreementRequestResponse.agreementId);
    console.log("freeTrialPricingTerm agreement entitlements are now active.");
    formatOutput(entitlementsResponse);

    // --- Step 2: Replace Agreement with freeTrialPricingTerm with Paid CCP Offer ---
    // Use Intent.REPLACE and sourceAgreementIdentifier to replace the free trial agreement.
    const usageBasedPricingTerm = { id: USAGE_BASED_PRICING_TERM_ID };
    const fixedUpfrontPricingTerm = { id: FIXED_UPFRONT_PRICING_TERM_ID };
    const paymentScheduleTerm = { id: PAYMENT_SCHEDULE_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };
    const newLegalTerm = { id: NEW_LEGAL_TERM_ID };

    const carResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "REPLACE",
            requestedTerms: [usageBasedPricingTerm, fixedUpfrontPricingTerm, paymentScheduleTerm, validityTerm, newLegalTerm],
            agreementProposalIdentifier: NEW_AGREEMENT_PROPOSAL_IDENTIFIER,
            sourceAgreementIdentifier: acceptAgreementRequestResponse.agreementId,
        })
    );
    console.log("Replace agreement request created. AgreementRequestId: " + carResponse.agreementRequestId);

    const aarResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carResponse.agreementRequestId,
        })
    );
    console.log("Agreement with freeTrialPricingTerm replaced with paid CCP offer. New AgreementId: " + aarResponse.agreementId);
}

createSaaSFreeTrialAndReplaceWithCCP();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Replace a SaaS usage-based pricing term and cancel the previous agreement
<a name="marketplace-agreement_ReplaceSaaSUsageBasedPricingTermAndCancel_javascript_topic"></a>

The following code example shows how to replace a SaaS usage-based pricing term and cancel the previous agreement.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
    CancelAgreementCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken, formatOutput, pollUntilEntitlementsAvailable } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to create a SaaS agreement with usageBasedPricingTerm (UBPT) and then replace it
 * with a new offer using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer subscribes to a SaaS product with UsageBasedPricingTerm.
 * The buyer then converts to a different offer by replacing the existing agreement.
 *
 * Flow:
 *   1. Create and accept the initial agreement request with UBPT.
 *   2. Wait for entitlements to become active.
 *   3. Replace the agreement with a new offer using Intent.REPLACE.
 *   4. Cancel the new agreement using CancelAgreement.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offers:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the initial offer.
 *   - NEW_AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the new offer to replace to.
 *   - Term IDs (starting with "term-") — found in each offer's term list.
 */

// The agreementProposalId from the initial offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the UsageBasedPricingTerm in the initial offer.
const USAGE_BASED_PRICING_TERM_ID = "<your-usage-based-pricing-term-id>";

// Term ID for the ValidityTerm in the initial offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

// Term ID for the LegalTerm in the initial offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// The agreementProposalId from the new offer to replace to.
const NEW_AGREEMENT_PROPOSAL_IDENTIFIER = "<your-new-agreement-proposal-identifier>";

// Term ID for the UsageBasedPricingTerm in the new offer.
const NEW_USAGE_BASED_PRICING_TERM_ID = "<your-new-usage-based-pricing-term-id>";

// Term ID for the ValidityTerm in the new offer.
const NEW_VALIDITY_TERM_ID = "<your-new-validity-term-id>";

// Term ID for the LegalTerm in the new offer.
const NEW_LEGAL_TERM_ID = "<your-new-legal-term-id>";

/**
 * Full end-to-end flow:
 * 1. Create and accept the initial agreement request with UsageBasedPricingTerm.
 * 2. Wait for entitlements to become active.
 * 3. Replace the agreement with a new offer.
 * 4. Cancel the new agreement.
 */
async function replaceSaaSUbptAndCancel() {
    const client = new MarketplaceAgreementClient();

    const usageBasedPricingTerm = { id: USAGE_BASED_PRICING_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };
    const legalTerm = { id: LEGAL_TERM_ID };

    // --- Step 1: Create and accept the initial UBPT agreement request ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [usageBasedPricingTerm, validityTerm, legalTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with UBPT created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    console.log("Agreement request with UBPT accepted. AgreementId: " + acceptAgreementRequestResponse.agreementId);

    // Wait for entitlements to become active before replacing.
    console.log("Waiting for entitlements to become active...");
    const entitlementsResponse = await pollUntilEntitlementsAvailable(client, acceptAgreementRequestResponse.agreementId);
    console.log("Entitlements are now active.");
    formatOutput(entitlementsResponse);

    // --- Step 2: Replace the UBPT agreement with a new offer ---
    // Use Intent.REPLACE and sourceAgreementIdentifier to replace the existing agreement.
    const newUsageBasedPricingTerm = { id: NEW_USAGE_BASED_PRICING_TERM_ID };
    const newValidityTerm = { id: NEW_VALIDITY_TERM_ID };
    const newLegalTerm = { id: NEW_LEGAL_TERM_ID };

    const carResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "REPLACE",
            requestedTerms: [newUsageBasedPricingTerm, newValidityTerm, newLegalTerm],
            agreementProposalIdentifier: NEW_AGREEMENT_PROPOSAL_IDENTIFIER,
            sourceAgreementIdentifier: acceptAgreementRequestResponse.agreementId,
        })
    );
    console.log("Replace agreement request created. AgreementRequestId: " + carResponse.agreementRequestId);

    const aarResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carResponse.agreementRequestId,
        })
    );
    const agreementIdWithTheNewOffer = aarResponse.agreementId;
    console.log("UBPT agreement replaced. New AgreementId: " + agreementIdWithTheNewOffer);

    // --- Step 3: Cancel the new agreement ---
    await client.send(
        new CancelAgreementCommand({
            agreementId: agreementIdWithTheNewOffer,
        })
    );
    console.log("The new agreement has been cancelled. AgreementId: " + agreementIdWithTheNewOffer);
}

replaceSaaSUbptAndCancel();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Replace an AMI usage-based pricing term but keep the ConfigurableUpfrontPricingTerm
<a name="marketplace-agreement_ReplaceAmiUsageBasedPricingTermButNotCupt_javascript_topic"></a>

The following code example shows how to replace an AMI usage-based pricing term while keeping the existing ConfigurableUpfrontPricingTerm.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken, formatOutput, pollUntilEntitlementsAvailable } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to replace an AMI agreement with usageBasedPricingTerm with a new offer while
 * the agreement with ConfigurableUpfrontPricingTerm (CUPT) is still active, using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: An AMI product with USAGE pricing requires two agreements:
 *   1. An agreement with usageBasedPricingTerm — accepted first to establish the base agreement.
 *   2. An agreement with configurableUpfrontPricingTerm (CUPT) — accepted after the usageBasedPricingTerm agreement entitlements are active.
 *
 * This sample shows how to replace only the agreement with usageBasedPricingTerm with a
 * new offer without touching the existing agreement with configurableUpfrontPricingTerm (CUPT).
 *
 * Flow:
 *   1. Create and accept the initial agreement request with usageBasedPricingTerm.
 *   2. Create and accept the agreement request with configurableUpfrontPricingTerm (CUPT) (after usageBasedPricingTerm agreement entitlements are active).
 *   3. Replace the agreement with usageBasedPricingTerm with a new offer using Intent.REPLACE.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offers:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the initial offer.
 *   - NEW_AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the new offer to replace to.
 *   - Term IDs (starting with "term-") — found in each offer's term list.
 *   - SELECTOR_VALUE — duration for the agreement (e.g., "P365D").
 *   - DIMENSION_1_KEY — dimension key defined in the CUPT term.
 */

// The agreementProposalId from the initial offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the ConfigurableUpfrontPricingTerm in the initial offer.
const CONFIGURABLE_UPFRONT_PRICING_TERM_ID = "<your-configurable-upfront-pricing-term-id>";

// Duration for the agreement (e.g., "P365D" for 365 days).
const SELECTOR_VALUE = "<your-selector-value>";

// Dimension key defined in the CUPT term.
const DIMENSION_1_KEY = "<your-dimension-key>";

// Quantity for the dimension.
const DIMENSION_1_VALUE = 1;

// Term ID for the UsageBasedPricingTerm in the initial offer.
const USAGE_TERM_ID = "<your-usage-term-id>";

// Term ID for the LegalTerm in the initial offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Term ID for the ValidityTerm in the initial offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

// The agreementProposalId from the new offer to replace to.
const NEW_AGREEMENT_PROPOSAL_IDENTIFIER = "<your-new-agreement-proposal-identifier>";

// Term ID for the UsageBasedPricingTerm in the new offer.
const NEW_USAGE_TERM_ID = "<your-new-usage-term-id>";

// Term ID for the LegalTerm in the new offer.
const NEW_LEGAL_TERM_ID = "<your-new-legal-term-id>";

// Term ID for the ValidityTerm in the new offer.
const NEW_VALIDITY_TERM_ID = "<your-new-validity-term-id>";

/**
 * Full end-to-end flow:
 * 1. Create and accept an agreement request with usageBasedPricingTerm, then wait for entitlements.
 * 2. Create and accept an agreement request with CUPT, then wait for entitlements.
 * 3. Replace the agreement with usageBasedPricingTerm with a new offer (agreement with CUPT is unaffected).
 */
async function replaceAmiUsageWhenCuptExists() {
    const client = new MarketplaceAgreementClient();

    const usageTerm = { id: USAGE_TERM_ID };
    const legalTerm = { id: LEGAL_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };

    // --- Step 1: Agreement with UBPT ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [usageTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with UBPT created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
        })
    );
    const usageAgreementId = acceptAgreementRequestResponse.agreementId;
    console.log("Agreement request with UBPT accepted. AgreementId: " + usageAgreementId);

    // Wait for UBPT agreement entitlements to become active before creating the agreement with CUPT.
    console.log("Waiting for UBPT agreement entitlements to become active...");
    const entitlementsResponse = await pollUntilEntitlementsAvailable(client, usageAgreementId);
    console.log("UBPT agreement entitlements are now active.");
    formatOutput(entitlementsResponse);

    // --- Step 2: Agreement with configurableUpfrontPricingTerm (CUPT) ---
    const configurableUpfrontPricingTerm = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: DIMENSION_1_VALUE },
                ],
            },
        },
    };

    const carResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [configurableUpfrontPricingTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request with CUPT created. AgreementRequestId: " + carResponse.agreementRequestId);

    const aarResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carResponse.agreementRequestId,
        })
    );
    const cuptAgreementId = aarResponse.agreementId;
    console.log("Agreement request with CUPT accepted. AgreementId: " + cuptAgreementId);

    // Wait for CUPT agreement entitlements to become active before replacing usage.
    console.log("Waiting for CUPT agreement entitlements to become active...");
    const cuptEntitlementsResponse = await pollUntilEntitlementsAvailable(client, cuptAgreementId);
    console.log("CUPT agreement entitlements are now active.");
    formatOutput(cuptEntitlementsResponse);

    // --- Step 3: Replace Agreement with usageBasedPricingTerm with a new offer ---
    const newUsageTerm = { id: NEW_USAGE_TERM_ID };
    const newLegalTerm = { id: NEW_LEGAL_TERM_ID };
    const newValidityTerm = { id: NEW_VALIDITY_TERM_ID };

    // Use Intent.REPLACE and sourceAgreementIdentifier pointing to the usageBasedPricingTerm agreement only.
    // The agreement with configurableUpfrontPricingTerm (CUPT) is NOT affected by this replacement.
    const carReplaceResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "REPLACE",
            requestedTerms: [newUsageTerm, newLegalTerm, newValidityTerm],
            agreementProposalIdentifier: NEW_AGREEMENT_PROPOSAL_IDENTIFIER,
            sourceAgreementIdentifier: usageAgreementId,
        })
    );
    console.log("Replace agreement request created. AgreementRequestId: " + carReplaceResponse.agreementRequestId);

    const aarReplaceResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: carReplaceResponse.agreementRequestId,
        })
    );
    console.log("Agreement with UBPT replaced. New AgreementId: " + aarReplaceResponse.agreementId);
}

replaceAmiUsageWhenCuptExists();
```
+  For API details, see [CreateAgreementRequest](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/CreateAgreementRequestCommand) in *AWS SDK for JavaScript API Reference*.

### Start the approval of an agreement request
<a name="marketplace-agreement_StartAgreementApprovals_javascript_topic"></a>

The following code example shows how to start the approval of an agreement request, optionally with purchase orders.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    StartAgreementApprovalsCommand,
} = require("@aws-sdk/client-marketplace-agreement");

const AGREEMENT_REQUEST_ID = "<AGREEMENT REQUEST ID HERE>";
// planReference of a plan returned by GetAgreementRequestApprovalPlans for this agreement request.
const PLAN_REFERENCE = "<PLAN REFERENCE HERE>";
const REQUESTER_NOTE = "<NOTE FOR THE APPROVERS HERE>";
// Optional: a purchase order for an expected charge, by its id from GetAgreementRequest chargeSummary.
const CHARGE_ID = undefined;
const PURCHASE_ORDER_REFERENCE = "<PURCHASE ORDER REFERENCE HERE>";

async function startAgreementApprovals() {
    const client = new MarketplaceAgreementClient();

    const response = await client.send(
        new StartAgreementApprovalsCommand({
            agreementRequestId: AGREEMENT_REQUEST_ID,
            planInputs: [
                {
                    buyerAgreementApprovalPlanInput: {
                        planReference: PLAN_REFERENCE,
                        requesterNote: REQUESTER_NOTE,
                    },
                },
            ],
            purchaseOrders: CHARGE_ID
                ? [{ chargeId: CHARGE_ID, purchaseOrderReference: PURCHASE_ORDER_REFERENCE }]
                : undefined,
        })
    );

    for (const summary of response.approvalSummaries) {
        console.log("Approval Type: " + summary.approvalType);
        console.log("Agreement Request ID: " + summary.agreementRequestId);
        console.log("Agreement Approval ID: " + summary.agreementApprovalId);
        console.log("Name: " + summary.name);
        console.log("Status: " + summary.status);
        console.log("Created At: " + summary.createdAt);
        console.log("Updated At: " + summary.updatedAt);
        console.log("Started At: " + summary.startedAt);
        console.log("Expires At: " + summary.expiresAt);
        console.log("Approval Needed By: " + summary.approvalNeededBy);
        console.log("---");
    }
}

startAgreementApprovals();
```
+  For API details, see [StartAgreementApprovals](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/StartAgreementApprovalsCommand) in *AWS SDK for JavaScript API Reference*.

### Update purchase orders after agreement acceptance
<a name="marketplace-agreement_UpdatePurchaseOrdersAfterAgreementAcceptance_javascript_topic"></a>

The following code example shows how to update purchase orders after the agreement has been accepted.

**SDK for JavaScript (v3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/javascript) repository.

```javascript
const {
    MarketplaceAgreementClient,
    CreateAgreementRequestCommand,
    AcceptAgreementRequestCommand,
    ListAgreementChargesCommand,
    UpdatePurchaseOrdersCommand,
} = require("@aws-sdk/client-marketplace-agreement");
const { generateClientToken, formatOutput } = require("./utils/AgreementApiUtils");

/**
 * Demonstrates how to associate a purchase order reference with a SaaS agreement with CONTRACT pricing model
 * using the AWS Marketplace Agreement Service APIs.
 *
 * Scenario: A buyer creates a SaaS agreement request with CONTRACT pricing model and provides a purchase order
 * reference in AcceptAgreementRequest. After acceptance, the buyer lists the resulting
 * charges via ListAgreementCharges and associates the purchase order reference with a
 * specific charge via UpdatePurchaseOrders.
 *
 * Before running this sample, replace the placeholder constants below with values from
 * your AWS Marketplace offer:
 *   - AGREEMENT_PROPOSAL_IDENTIFIER — the agreementProposalId from the offer.
 *   - Term IDs (starting with "term-") — found in the offer's term list.
 *   - SELECTOR_VALUE — duration for the agreement.
 *   - DIMENSION_1_KEY — dimension key defined in the offer.
 *   - PURCHASE_ORDER_REFERENCE — your internal purchase order number (e.g., "po-123456").
 */

// Your internal purchase order reference number (e.g., "po-123456").
const PURCHASE_ORDER_REFERENCE = "po-123456";

// The agreementProposalId from the offer.
const AGREEMENT_PROPOSAL_IDENTIFIER = "<your-agreement-proposal-identifier>";

// Term ID for the ConfigurableUpfrontPricingTerm in your offer.
const CONFIGURABLE_UPFRONT_PRICING_TERM_ID = "<your-configurable-upfront-pricing-term-id>";

// Duration for the agreement (e.g., "P366D" for 366 days).
const SELECTOR_VALUE = "<your-selector-value>";

// Dimension key and quantity defined in your offer.
const DIMENSION_1_KEY = "<your-dimension-key>";
const DIMENSION_1_VALUE = 1;

// Term ID for the LegalTerm in your offer.
const LEGAL_TERM_ID = "<your-legal-term-id>";

// Term ID for the ValidityTerm in your offer.
const VALIDITY_TERM_ID = "<your-validity-term-id>";

/**
 * Full end-to-end flow:
 * 1. Create a SaaS agreement with CONTRACT pricing model with a purchase order reference.
 * 2. List charges to retrieve charge IDs and revisions.
 * 3. Associate the purchase order reference with a specific charge via UpdatePurchaseOrders.
 * 4. List charges again to confirm the update.
 */
async function listAgreementChargesAndUpdatePurchaseOrders() {
    const client = new MarketplaceAgreementClient();

    const configurableUpfrontPricingTerm = {
        id: CONFIGURABLE_UPFRONT_PRICING_TERM_ID,
        configuration: {
            configurableUpfrontPricingTermConfiguration: {
                selectorValue: SELECTOR_VALUE,
                dimensions: [
                    { dimensionKey: DIMENSION_1_KEY, dimensionValue: DIMENSION_1_VALUE },
                ],
            },
        },
    };

    const legalTerm = { id: LEGAL_TERM_ID };
    const validityTerm = { id: VALIDITY_TERM_ID };

    // --- Create Agreement ---
    const createAgreementRequestResponse = await client.send(
        new CreateAgreementRequestCommand({
            clientToken: generateClientToken(),
            intent: "NEW",
            requestedTerms: [configurableUpfrontPricingTerm, legalTerm, validityTerm],
            agreementProposalIdentifier: AGREEMENT_PROPOSAL_IDENTIFIER,
        })
    );
    console.log("Agreement request created. AgreementRequestId: " + createAgreementRequestResponse.agreementRequestId);

    // --- Accept Agreement Request with Purchase Order ---
    // The chargeId is available from the CAR response's chargeSummary.expectedCharges.
    const chargeId = createAgreementRequestResponse.chargeSummary.expectedCharges[0].id;
    const purchaseOrderAtAcceptance = {
        chargeId: chargeId,
        purchaseOrderReference: PURCHASE_ORDER_REFERENCE,
    };
    const acceptAgreementRequestResponse = await client.send(
        new AcceptAgreementRequestCommand({
            agreementRequestId: createAgreementRequestResponse.agreementRequestId,
            purchaseOrders: [purchaseOrderAtAcceptance],
        })
    );
    const agreementId = acceptAgreementRequestResponse.agreementId;
    console.log("Agreement request accepted with purchase order reference '" + PURCHASE_ORDER_REFERENCE
        + "'. AgreementId: " + agreementId);

    // --- List Agreement Charges ---
    const listAgreementChargesResponse = await client.send(
        new ListAgreementChargesCommand({
            agreementId: agreementId,
        })
    );

    console.log("All charges for agreement " + agreementId + ":");
    formatOutput(listAgreementChargesResponse);

    // --- Update Purchase Order ---
    const firstCharge = listAgreementChargesResponse.items[0];
    const purchaseOrder = {
        agreementId: agreementId,
        purchaseOrderReference: PURCHASE_ORDER_REFERENCE,
        chargeRevision: firstCharge.revision,
        chargeId: firstCharge.id,
    };
    await client.send(
        new UpdatePurchaseOrdersCommand({
            purchaseOrders: [purchaseOrder],
        })
    );
    console.log("Purchase order reference '" + PURCHASE_ORDER_REFERENCE
        + "' updated for ChargeId: " + firstCharge.id);

    // --- Verify Update ---
    const lacResponse = await client.send(
        new ListAgreementChargesCommand({
            agreementId: agreementId,
        })
    );
    console.log("Verified updated charge:");
    formatOutput(lacResponse.items[0]);
}

listAgreementChargesAndUpdatePurchaseOrders();
```
+  For API details, see [UpdatePurchaseOrders](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/marketplace-agreement/command/UpdatePurchaseOrdersCommand) in *AWS SDK for JavaScript API Reference*.
