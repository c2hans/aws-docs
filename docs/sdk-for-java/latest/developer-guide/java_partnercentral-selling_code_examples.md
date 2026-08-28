---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_partnercentral-selling_code_examples.html
---

# Partner Central examples using SDK for Java 2.x
<a name="java_partnercentral-selling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with Partner Central.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `AssignOpportunity`
<a name="partnercentral-selling_AssignOpportunity_java_topic"></a>

The following code example shows how to use `AssignOpportunity`.

**SDK for Java 2.x**
Reassign an existing Opportunity to another user.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AssignOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.AssignOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.AssigneeContact;

/*
Purpose
PC-API-07 Assigning a new owner
*/

public class AssignOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String assigneeFirstName = "John";

    	String assigneeLastName = "Doe";

    	String assigneeEmail = "test@test.com";

    	String businessTitle = "PartnerAccountManager";

    	AssignOpportunityResponse response = getResponse(opportunityId, assigneeFirstName, assigneeLastName, assigneeEmail, businessTitle);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static AssignOpportunityResponse getResponse(String opportunityId, String assigneeFirstName, String assigneeLastName, String assigneeEmail, String businessTitle) {

		AssignOpportunityRequest assignOpportunityRequest = AssignOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.assignee(AssigneeContact.builder()
        				.firstName(assigneeFirstName)
        				.lastName(assigneeLastName)
        				.email(assigneeEmail)
        				.businessTitle(businessTitle)
        				.build())
        		.build();

        AssignOpportunityResponse response = client.assignOpportunity(assignOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [AssignOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssignOpportunity) in *AWS SDK for Java 2.x API Reference*.

### `AssociateOpportunity`
<a name="partnercentral-selling_AssociateOpportunity_java_topic"></a>

The following code example shows how to use `AssociateOpportunity`.

**SDK for Java 2.x**
Create a formal association between an Opportunity and various related entities.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityResponse;

/*
Purpose
PC-API -11 Associating a product
PC-API -12 Associating a solution
PC-API -13 Associating an offer
entity_type = Solutions | AWSProducts | AWSMarketplaceOffers
*/

public class AssociateOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String entityType = "Solutions";

    	String entityIdentifier = "S-0000000";

    	AssociateOpportunityResponse response = getResponse(opportunityId, entityType, entityIdentifier );

    	ReferenceCodesUtils.formatOutput(response);
    }

static AssociateOpportunityResponse getResponse(String opportunityId, String entityType, String entityIdentifier) {

        AssociateOpportunityRequest associateOpportunityRequest = AssociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();

        AssociateOpportunityResponse response = client.associateOpportunity(associateOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [AssociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity) in *AWS SDK for Java 2.x API Reference*.

### `CreateOpportunity`
<a name="partnercentral-selling_CreateOpportunity_java_topic"></a>

The following code example shows how to use `CreateOpportunity`.

**SDK for Java 2.x**
Create an opportunity.

```
package org.example;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

import static org.example.utils.Constants.*;

import org.example.entity.Root;
import org.example.utils.ReferenceCodesUtils;
import org.example.utils.StringSerializer;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.Account;
import software.amazon.awssdk.services.partnercentralselling.model.Address;
import software.amazon.awssdk.services.partnercentralselling.model.Contact;
import software.amazon.awssdk.services.partnercentralselling.model.CreateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.CreateOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.Customer;
import software.amazon.awssdk.services.partnercentralselling.model.ExpectedCustomerSpend;
import software.amazon.awssdk.services.partnercentralselling.model.LifeCycle;
import software.amazon.awssdk.services.partnercentralselling.model.Marketing;
import software.amazon.awssdk.services.partnercentralselling.model.MonetaryValue;
import software.amazon.awssdk.services.partnercentralselling.model.NextStepsHistory;
import software.amazon.awssdk.services.partnercentralselling.model.Project;
import software.amazon.awssdk.services.partnercentralselling.model.SoftwareRevenue;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.ToNumberPolicy;

public class CreateOpportunity {

	static final Gson GSON = new GsonBuilder()
			.setObjectToNumberStrategy(ToNumberPolicy.LAZILY_PARSED_NUMBER)
			.registerTypeAdapter(String.class, new StringSerializer())
			.create();

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

	public static void main(String[] args) {

		String inputFile = "CreateOpportunity2.json";

		if (args.length > 0)
			inputFile = args[0];

		CreateOpportunityResponse response = createOpportunity(inputFile);

		client.close();
	}

	static CreateOpportunityResponse createOpportunity(String inputFile) {

		String inputString = ReferenceCodesUtils.readInputFileToString(inputFile);

		Root root = GSON.fromJson(inputString, Root.class);

		List<NextStepsHistory> nextStepsHistories = new ArrayList<NextStepsHistory>();
		if ( root.lifeCycle != null && root.lifeCycle.nextStepsHistories != null) {
			for (org.example.entity.NextStepsHistory nextStepsHistoryJson : root.lifeCycle.nextStepsHistories) {
				NextStepsHistory nextStepsHistory = NextStepsHistory.builder()
						.time(Instant.parse(nextStepsHistoryJson.time))
						.value(nextStepsHistoryJson.value)
		                .build();
				nextStepsHistories.add(nextStepsHistory);
			}
		}

		LifeCycle lifeCycle = null;
		if ( root.lifeCycle != null ) {
			lifeCycle = LifeCycle.builder()
				.closedLostReason(root.lifeCycle.closedLostReason)
				.nextSteps(root.lifeCycle.nextSteps)
				.nextStepsHistory(nextStepsHistories)
				.reviewComments(root.lifeCycle.reviewComments)
				.reviewStatus(root.lifeCycle.reviewStatus)
				.reviewStatusReason(root.lifeCycle.reviewStatusReason)
				.stage(root.lifeCycle.stage)
				.targetCloseDate(root.lifeCycle.targetCloseDate)
				.build();
		}

		Marketing marketing = null;
		if ( root.marketing != null ) {
			marketing = Marketing.builder()
					.awsFundingUsed(root.marketing.awsFundingUsed)
					.campaignName(root.marketing.campaignName)
					.channels(root.marketing.channels)
					.source(root.marketing.source)
					.useCases(root.marketing.useCases)
					.build();

		}

		Address address = null;
		if ( root.customer != null && root.customer.account != null && root.customer.account.address != null ) {
			address = Address.builder()
				.city(root.customer.account.address.city)
                .postalCode(root.customer.account.address.postalCode)
                .stateOrRegion(root.customer.account.address.stateOrRegion)
                .countryCode(root.customer.account.address.countryCode)
                .streetAddress(root.customer.account.address.streetAddress)
                .build();
		}

		Account account = null;
		if ( root.customer != null && root.customer.account!= null) {
			account = Account.builder()
	            .address(address)
	            .awsAccountId(root.customer.account.awsAccountId)
                .duns(root.customer.account.duns)
                .industry(root.customer.account.industry)
                .otherIndustry(root.customer.account.otherIndustry)
                .companyName(root.customer.account.companyName)
                .websiteUrl(root.customer.account.websiteUrl)
                .build();
		}

		List<Contact> contacts = new ArrayList<Contact>();
		if ( root.customer != null && root.customer.contacts != null) {
			for (org.example.entity.Contact jsonContact : root.customer.contacts) {
				Contact contact = Contact.builder()
		                .email(jsonContact.email)
		                .firstName(jsonContact.firstName)
		                .lastName(jsonContact.lastName)
		                .phone(jsonContact.phone)
		                .businessTitle(jsonContact.businessTitle)
		                .build();
				contacts.add(contact);
			}
		}

		Customer customer = Customer.builder()
				.account(account)
				.contacts(contacts)
				.build();

		Contact oportunityTeamContact = null;
		if (root.opportunityTeam != null && root.opportunityTeam.get(0) != null ) {
			oportunityTeamContact = Contact.builder()
                .firstName(root.opportunityTeam.get(0).firstName)
                .lastName(root.opportunityTeam.get(0).lastName)
                .email(root.opportunityTeam.get(0).email)
                .phone(root.opportunityTeam.get(0).phone)
                .businessTitle(root.opportunityTeam.get(0).businessTitle)
                .build();
		}

		List<ExpectedCustomerSpend> expectedCustomerSpends = new ArrayList<ExpectedCustomerSpend>();
		if ( root.project != null && root.project.expectedCustomerSpend != null) {
			for (org.example.entity.ExpectedCustomerSpend expectedCustomerSpendJson : root.project.expectedCustomerSpend) {
				ExpectedCustomerSpend expectedCustomerSpend = null;
				expectedCustomerSpend = ExpectedCustomerSpend.builder()
						.amount(expectedCustomerSpendJson.amount)
						.currencyCode(expectedCustomerSpendJson.currencyCode)
						.frequency(expectedCustomerSpendJson.frequency)
						.targetCompany(expectedCustomerSpendJson.targetCompany)
						.build();
				expectedCustomerSpends.add(expectedCustomerSpend);
			}
        }

        Project project = null;
        if ( root.project != null) {
        	project = Project.builder()
                .title(root.project.title)
                .customerBusinessProblem(root.project.customerBusinessProblem)
                .customerUseCase(root.project.customerUseCase)
                .deliveryModels(root.project.deliveryModels)
                .expectedCustomerSpend(expectedCustomerSpends)
                .salesActivities(root.project.salesActivities)
                .competitorName(root.project.competitorName)
                .otherSolutionDescription(root.project.otherSolutionDescription)
                .build();
        }

        SoftwareRevenue softwareRevenue = null;
        if ( root.softwareRevenue != null) {
        	MonetaryValue monetaryValue = null;
        	if ( root.softwareRevenue.value != null) {
        		monetaryValue = MonetaryValue.builder()
        				.amount(root.softwareRevenue.value.amount)
        				.currencyCode(root.softwareRevenue.value.currencyCode)
        				.build();
        	}
        	softwareRevenue = SoftwareRevenue.builder()
        			.deliveryModel(root.softwareRevenue.deliveryModel)
        			.effectiveDate(root.softwareRevenue.effectiveDate)
        			.expirationDate(root.softwareRevenue.expirationDate)
        			.value(monetaryValue)
        			.build();
        }

		// Building the Actual CreateOpportunity Request
		CreateOpportunityRequest createOpportunityRequest = CreateOpportunityRequest.builder()
				.catalog(CATALOG_TO_USE)
				.clientToken(root.clientToken)
				.primaryNeedsFromAwsWithStrings(root.primaryNeedsFromAws)
				.opportunityType(root.opportunityType)
				.lifeCycle(lifeCycle)
				.marketing(marketing)
				.nationalSecurity(root.nationalSecurity)
				.origin(root.origin)
				.customer(customer)
				.project(project)
				.partnerOpportunityIdentifier(root.partnerOpportunityIdentifier)
				.opportunityTeam(oportunityTeamContact)
				.softwareRevenue(softwareRevenue)
				.build();

		CreateOpportunityResponse response = client.createOpportunity(createOpportunityRequest);
		System.out.println("Successfully created: " + response);

		return response;
    }

}
```
+  For API details, see [CreateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CreateOpportunity) in *AWS SDK for Java 2.x API Reference*.

### `DisassociateOpportunity`
<a name="partnercentral-selling_DisassociateOpportunity_java_topic"></a>

The following code example shows how to use `DisassociateOpportunity`.

**SDK for Java 2.x**
Remove an existing association between an Opportunity and related entities.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityResponse;

/*
Purpose
PC-API -14 Removing a Solution
PC-API -15 Removing an offer
PC-API -16 Removing a product
entity_type = Solutions | AWSProducts | AWSMarketplaceOffers
*/

public class DisassociateOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String entityType = "Solutions";

    	String entityIdentifier = "S-0000000";

    	DisassociateOpportunityResponse response = getResponse(opportunityId, entityType, entityIdentifier );

    	ReferenceCodesUtils.formatOutput(response);
    }

	static DisassociateOpportunityResponse getResponse(String opportunityId, String entityType, String entityIdentifier) {

		DisassociateOpportunityRequest disassociateOpportunityRequest = DisassociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();

        DisassociateOpportunityResponse response = client.disassociateOpportunity(disassociateOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [DisassociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity) in *AWS SDK for Java 2.x API Reference*.

### `GetAwsOpportunitySummary`
<a name="partnercentral-selling_GetAwsOpportunitySummary_java_topic"></a>

The following code example shows how to use `GetAwsOpportunitySummary`.

**SDK for Java 2.x**
Retrieves a summary of an AWS Opportunity.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.GetAwsOpportunitySummaryRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetAwsOpportunitySummaryResponse;

/*
 * Purpose
 * PC-API-25 Retrieves a summary of an AWS Opportunity.
 */

public class GetAwsOpportunitySummary {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	GetAwsOpportunitySummaryResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	public static GetAwsOpportunitySummaryResponse getResponse(String opportunityId) {

		GetAwsOpportunitySummaryRequest getOpportunityRequest = GetAwsOpportunitySummaryRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.relatedOpportunityIdentifier(opportunityId)
        		.build();

		GetAwsOpportunitySummaryResponse response = client.getAwsOpportunitySummary(getOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [GetAwsOpportunitySummary](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetAwsOpportunitySummary) in *AWS SDK for Java 2.x API Reference*.

### `GetEngagementInvitation`
<a name="partnercentral-selling_GetEngagementInvitation_java_topic"></a>

The following code example shows how to use `GetEngagementInvitation`.

**SDK for Java 2.x**
Retrieves the details of an engagement invitation shared by AWS with a partner.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.GetEngagementInvitationRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetEngagementInvitationResponse;

/*
 * Purpose
 * PC-API-22 Get engagement invitation opportunity
 */

public class GetEngagementInvitation {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	GetEngagementInvitationResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static GetEngagementInvitationResponse getResponse(String opportunityId) {

		GetEngagementInvitationRequest getOpportunityRequest = GetEngagementInvitationRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.build();

		GetEngagementInvitationResponse response = client.getEngagementInvitation(getOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [GetEngagementInvitation](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetEngagementInvitation) in *AWS SDK for Java 2.x API Reference*.

### `GetOpportunity`
<a name="partnercentral-selling_GetOpportunity_java_topic"></a>

The following code example shows how to use `GetOpportunity`.

**SDK for Java 2.x**
Get an opportunity.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityResponse;

/*
 * Purpose
 * PC-API-08 Get updated Opportunity
 */

public class GetOpportunity {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	GetOpportunityResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	public static GetOpportunityResponse getResponse(String opportunityId) {

        GetOpportunityRequest getOpportunityRequest = GetOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.build();

        GetOpportunityResponse response = client.getOpportunity(getOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [GetOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/GetOpportunity) in *AWS SDK for Java 2.x API Reference*.

### `ListEngagementInvitations`
<a name="partnercentral-selling_ListEngagementInvitations_java_topic"></a>

The following code example shows how to use `ListEngagementInvitations`.

**SDK for Java 2.x**
Retrieves a list of engagement invitations sent to the partner.

```
package org.example;

import java.util.ArrayList;
import java.util.List;

import org.example.utils.ReferenceCodesUtils;
import static org.example.utils.Constants.*;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.ListEngagementInvitationsRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListEngagementInvitationsResponse;
import software.amazon.awssdk.services.partnercentralselling.model.ParticipantType;
import software.amazon.awssdk.services.partnercentralselling.model.EngagementInvitationSummary;

public class ListEngagementInvitations {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	List<EngagementInvitationSummary> opportunitySummaries = getResponse();
        ReferenceCodesUtils.formatOutput(opportunitySummaries);
    }

    static List<EngagementInvitationSummary> getResponse() {

		List<EngagementInvitationSummary> opportunitySummaries = new ArrayList<EngagementInvitationSummary>();

		ListEngagementInvitationsRequest listOpportunityRequest = ListEngagementInvitationsRequest.builder()
                .catalog(CATALOG_TO_USE)
                .participantType(ParticipantType.RECEIVER)
        		.maxResults(5)
        		.build();

		ListEngagementInvitationsResponse response = client.listEngagementInvitations(listOpportunityRequest);

    	opportunitySummaries.addAll(response.engagementInvitationSummaries());

    	client.close();

        return opportunitySummaries;
	}
}
```
+  For API details, see [ListEngagementInvitations](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementInvitations) in *AWS SDK for Java 2.x API Reference*.

### `ListOpportunities`
<a name="partnercentral-selling_ListOpportunities_java_topic"></a>

The following code example shows how to use `ListOpportunities`.

**SDK for Java 2.x**
List opportunities.

```
package org.example;

import java.util.ArrayList;
import java.util.List;

import org.example.utils.ReferenceCodesUtils;
import static org.example.utils.Constants.*;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.ListOpportunitiesRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListOpportunitiesResponse;
import software.amazon.awssdk.services.partnercentralselling.model.OpportunitySummary;

/*
 * Purpose
 * PC-API-18 Getting list of Opportunities
 */

public class ListOpportunititesPaging {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {
    	List<OpportunitySummary> opportunitySummaries = getResponse();
        ReferenceCodesUtils.formatOutput(opportunitySummaries);
    }

    private static List<OpportunitySummary> getResponse() {
    	List<OpportunitySummary> opportunitySummaries = new ArrayList<OpportunitySummary>();

		ListOpportunitiesRequest listOpportunityRequest = ListOpportunitiesRequest.builder()
                .catalog(CATALOG_TO_USE)
        		.maxResults(5)
        		.build();

    	ListOpportunitiesResponse response = client.listOpportunities(listOpportunityRequest);

    	opportunitySummaries.addAll(response.opportunitySummaries());

    	while (response.nextToken() != null && response.nextToken().length() > 0) {
    		listOpportunityRequest = ListOpportunitiesRequest.builder()
                    .catalog(CATALOG_TO_USE)
            		.maxResults(5)
            		.nextToken(response.nextToken())
            		.build();
    		response = client.listOpportunities(listOpportunityRequest);
    		opportunitySummaries.addAll(response.opportunitySummaries());
    	}

    	client.close();

        return opportunitySummaries;
	}
}
```
+  For API details, see [ListOpportunities](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunities) in *AWS SDK for Java 2.x API Reference*.

### `ListSolutions`
<a name="partnercentral-selling_ListSolutions_java_topic"></a>

The following code example shows how to use `ListSolutions`.

**SDK for Java 2.x**
Retrieves a list of Partner Solutions that the partner registered on Partner Central.

```
package org.example;

import java.util.ArrayList;
import java.util.List;

import static org.example.utils.Constants.*;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.ListSolutionsRequest;
import software.amazon.awssdk.services.partnercentralselling.model.ListSolutionsResponse;
import software.amazon.awssdk.services.partnercentralselling.model.SolutionBase;

/*
 * Purpose
 * PC-API-10 Getting list of solutions
 */

public class ListSolutions {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {
    	List<SolutionBase> solutionSummaries = getResponse();
        ReferenceCodesUtils.formatOutput(solutionSummaries);
    }

    static List<SolutionBase> getResponse() {
		List<SolutionBase> solutionSummaries = new ArrayList<SolutionBase>();

		ListSolutionsRequest listSolutionsRequest = ListSolutionsRequest.builder()
				.catalog(CATALOG_TO_USE)
        		.maxResults(5)
        		.build();

    	ListSolutionsResponse response = client.listSolutions(listSolutionsRequest);

    	solutionSummaries.addAll(response.solutionSummaries());

        return solutionSummaries;
	}
}
```
+  For API details, see [ListSolutions](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListSolutions) in *AWS SDK for Java 2.x API Reference*.

### `RejectEngagementInvitation`
<a name="partnercentral-selling_RejectEngagementInvitation_java_topic"></a>

The following code example shows how to use `RejectEngagementInvitation`.

**SDK for Java 2.x**
Rejects an EngagementInvitation that AWS shared.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.RejectEngagementInvitationRequest;
import software.amazon.awssdk.services.partnercentralselling.model.RejectEngagementInvitationResponse;

/*
 * Purpose
 * PC-API-05 AWS Originated(AO) rejection
 */

public class RejectEngagementInvitation {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

		RejectEngagementInvitationResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static RejectEngagementInvitationResponse getResponse(String invitationId) {

        RejectEngagementInvitationRequest rejectOpportunityRequest = RejectEngagementInvitationRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(invitationId)
        		.rejectionReason("Unable to support")
        		.build();

		RejectEngagementInvitationResponse response = client.rejectEngagementInvitation(rejectOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [RejectEngagementInvitation](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/RejectEngagementInvitation) in *AWS SDK for Java 2.x API Reference*.

### `StartEngagementByAcceptingInvitationTask`
<a name="partnercentral-selling_StartEngagementByAcceptingInvitationTask_java_topic"></a>

The following code example shows how to use `StartEngagementByAcceptingInvitationTask`.

**SDK for Java 2.x**
Starts the engagement by accepting an EngagementInvitation.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementByAcceptingInvitationTaskRequest;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementByAcceptingInvitationTaskResponse;
import software.amazon.awssdk.services.partnercentralselling.model.GetEngagementInvitationRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetEngagementInvitationResponse;
import software.amazon.awssdk.services.partnercentralselling.model.InvitationStatus;

/*
Purpose
PC-API-04: Start Engagement By Accepting InvitationTask for AWS Originated(AO) opportunity
*/

public class StartEngagementByAcceptingInvitationTask {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

	static String clientToken = "test-a30d161";

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	StartEngagementByAcceptingInvitationTaskResponse response = getResponse(opportunityId);

    	if ( response == null) {
    		System.out.println("Opportunity is not AWS Originated.");
    	} else {
    		ReferenceCodesUtils.formatOutput(response);
    	}
    }

    private static GetEngagementInvitationResponse getInvitation(String invitationId) {

    	GetEngagementInvitationRequest getRequest = GetEngagementInvitationRequest.builder()
        		.catalog(Constants.CATALOG_TO_USE)
        		.identifier(invitationId)
        		.build();

		GetEngagementInvitationResponse response = client.getEngagementInvitation(getRequest);

        return response;
	}

	static StartEngagementByAcceptingInvitationTaskResponse getResponse(String invitationId) {

		if ( getInvitation(invitationId).status().equals(InvitationStatus.PENDING)) {
			StartEngagementByAcceptingInvitationTaskRequest acceptOpportunityRequest =
					StartEngagementByAcceptingInvitationTaskRequest.builder()
					.catalog(Constants.CATALOG_TO_USE)
	        		.identifier(invitationId)
	        		.clientToken(clientToken)
	        		.build();

			StartEngagementByAcceptingInvitationTaskResponse response = client.startEngagementByAcceptingInvitationTask(acceptOpportunityRequest);
	        return response;
		}
		return null;
	}
}
```
+  For API details, see [StartEngagementByAcceptingInvitationTask](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartEngagementByAcceptingInvitationTask) in *AWS SDK for Java 2.x API Reference*.

### `StartEngagementFromOpportunityTask`
<a name="partnercentral-selling_StartEngagementFromOpportunityTask_java_topic"></a>

The following code example shows how to use `StartEngagementFromOpportunityTask`.

**SDK for Java 2.x**
Initiates the engagement process from an existing opportunity by accepting the engagement invitation and creating a corresponding opportunity in the partner’s system.

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AwsSubmission;
import software.amazon.awssdk.services.partnercentralselling.model.SalesInvolvementType;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementFromOpportunityTaskRequest;
import software.amazon.awssdk.services.partnercentralselling.model.StartEngagementFromOpportunityTaskResponse;
import software.amazon.awssdk.services.partnercentralselling.model.Visibility;

/*
 * Purpose
 * PC-API-01 Partner Originated (PO) opp submission(Start Engagement From Opportunity Task for AO Originated Opportunity)
 */

public class StartEngagementFromOpportunityTask {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	StartEngagementFromOpportunityTaskResponse response = getResponse(opportunityId);

    	ReferenceCodesUtils.formatOutput(response);
    }

	static StartEngagementFromOpportunityTaskResponse getResponse(String opportunityId) {

		StartEngagementFromOpportunityTaskRequest submitOpportunityRequest = StartEngagementFromOpportunityTaskRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.clientToken("test-annjqwesdsd99")
        		.awsSubmission(AwsSubmission.builder().involvementType(SalesInvolvementType.CO_SELL).visibility(Visibility.FULL).build())
        		.build();

		StartEngagementFromOpportunityTaskResponse response = client.startEngagementFromOpportunityTask(submitOpportunityRequest);

        return response;
	}
}
```
+  For API details, see [StartEngagementFromOpportunityTask](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/StartEngagementFromOpportunityTask) in *AWS SDK for Java 2.x API Reference*.

### `UpdateOpportunity`
<a name="partnercentral-selling_UpdateOpportunity_java_topic"></a>

The following code example shows how to use `UpdateOpportunity`.

**SDK for Java 2.x**
Update an opportunity.

```
package org.example;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

import static org.example.utils.Constants.*;

import org.example.entity.Root;
import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;
import org.example.utils.StringSerializer;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.Account;
import software.amazon.awssdk.services.partnercentralselling.model.Address;
import software.amazon.awssdk.services.partnercentralselling.model.Contact;
import software.amazon.awssdk.services.partnercentralselling.model.Customer;
import software.amazon.awssdk.services.partnercentralselling.model.ExpectedCustomerSpend;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.GetOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.LifeCycle;
import software.amazon.awssdk.services.partnercentralselling.model.Marketing;
import software.amazon.awssdk.services.partnercentralselling.model.NextStepsHistory;
import software.amazon.awssdk.services.partnercentralselling.model.Project;
import software.amazon.awssdk.services.partnercentralselling.model.ReviewStatus;
import software.amazon.awssdk.services.partnercentralselling.model.UpdateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.UpdateOpportunityResponse;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.ToNumberPolicy;

/*
 * Purpose
 * PC-API-02/06 Update opportunity when LifeCycle.ReviewStatus is not Submitted or In-Review
 */

public class UpdateOpportunity {

	static final Gson GSON = new GsonBuilder()
			.setObjectToNumberStrategy(ToNumberPolicy.LAZILY_PARSED_NUMBER)
			.registerTypeAdapter(String.class, new StringSerializer())
			.create();

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

	static String OPPORTUNITY_ORIGIN = ORIGIN_PARTNER_ORIGINATED;

	public static void main(String[] args) {

		String inputFile = "updateOpportunity.json";

		if (args.length > 0)
			inputFile = args[0];

		UpdateOpportunityResponse response = updateOpportunity(inputFile);

		client.close();
	}

	public static GetOpportunityResponse getResponse(String opportunityId) {

        GetOpportunityRequest getOpportunityRequest = GetOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.identifier(opportunityId)
        		.build();

        GetOpportunityResponse response = client.getOpportunity(getOpportunityRequest);
        System.out.println(opportunityId + ":" + response);
        return response;
	}

	public static UpdateOpportunityResponse updateOpportunity(String inputFile) {

		String inputString = ReferenceCodesUtils.readInputFileToString(inputFile);

		Root root = GSON.fromJson(inputString, Root.class);
		GetOpportunityResponse response = getResponse(root.identifier);

		if (response != null
				&& response.lifeCycle() != null
				&& response.lifeCycle().reviewStatus() != null
				&& response.lifeCycle().reviewStatus() != ReviewStatus.SUBMITTED
				&& response.lifeCycle().reviewStatus() != ReviewStatus.IN_REVIEW) {

			List<NextStepsHistory> nextStepsHistories = new ArrayList<NextStepsHistory>();
			if ( root.lifeCycle != null && root.lifeCycle.nextStepsHistories != null) {
				for (org.example.entity.NextStepsHistory nextStepsHistoryJson : root.lifeCycle.nextStepsHistories) {
					NextStepsHistory nextStepsHistory = NextStepsHistory.builder()
							.time(Instant.parse(nextStepsHistoryJson.time))
							.value(nextStepsHistoryJson.value)
			                .build();
					nextStepsHistories.add(nextStepsHistory);
				}
			}

			LifeCycle lifeCycle = null;
			if ( root.lifeCycle != null ) {
				lifeCycle = LifeCycle.builder()
					.closedLostReason(root.lifeCycle.closedLostReason)
					.nextSteps(root.lifeCycle.nextSteps)
					.nextStepsHistory(nextStepsHistories)
					.reviewComments(root.lifeCycle.reviewComments)
					.reviewStatus(root.lifeCycle.reviewStatus)
					.reviewStatusReason(root.lifeCycle.reviewStatusReason)
					.stage(root.lifeCycle.stage)
					.targetCloseDate(root.lifeCycle.targetCloseDate)
					.build();
			}

			Marketing marketing = null;
			if ( root.marketing != null ) {
				marketing = Marketing.builder()
						.awsFundingUsed(root.marketing.awsFundingUsed)
						.campaignName(root.marketing.campaignName)
						.channels(root.marketing.channels)
						.source(root.marketing.source)
						.useCases(root.marketing.useCases)
						.build();

			}

			Address address = null;
			if (root.customer != null && root.customer.account != null && root.customer.account.address != null) {
				address = Address.builder().postalCode(root.customer.account.address.postalCode)
						.stateOrRegion(root.customer.account.address.stateOrRegion)
						.countryCode(root.customer.account.address.countryCode).build();
			}

			Account account = null;
			if (root.customer != null && root.customer.account != null) {
				account = Account.builder().address(address).duns(root.customer.account.duns)
						.industry(root.customer.account.industry).companyName(root.customer.account.companyName)
						.websiteUrl(root.customer.account.websiteUrl).build();
			}

			List<Contact> contacts = new ArrayList<Contact>();
			if ( root.customer != null && root.customer.contacts != null) {
				for (org.example.entity.Contact jsonContact : root.customer.contacts) {
					Contact contact = Contact.builder()
			                .email(jsonContact.email)
			                .firstName(jsonContact.firstName)
			                .lastName(jsonContact.lastName)
			                .phone(jsonContact.phone)
			                .businessTitle(jsonContact.businessTitle)
			                .build();
					contacts.add(contact);
				}
			}

			Customer customer = Customer.builder().account(account).contacts(contacts).build();

			List<ExpectedCustomerSpend> expectedCustomerSpends = new ArrayList<ExpectedCustomerSpend>();
			if ( root.project != null && root.project.expectedCustomerSpend != null) {
				for (org.example.entity.ExpectedCustomerSpend expectedCustomerSpendJson : root.project.expectedCustomerSpend) {
					ExpectedCustomerSpend expectedCustomerSpend = null;
					expectedCustomerSpend = ExpectedCustomerSpend.builder()
							.amount(expectedCustomerSpendJson.amount)
							.currencyCode(expectedCustomerSpendJson.currencyCode)
							.frequency(expectedCustomerSpendJson.frequency)
							.targetCompany(expectedCustomerSpendJson.targetCompany)
							.build();
					expectedCustomerSpends.add(expectedCustomerSpend);
				}
	        }

			Project project = null;
			if (root.project != null) {
				project = Project.builder().title(root.project.title)
						.customerBusinessProblem(root.project.customerBusinessProblem)
						.customerUseCase(root.project.customerUseCase).deliveryModels(root.project.deliveryModels)
						.expectedCustomerSpend(expectedCustomerSpends)
						.salesActivities(root.project.salesActivities).competitorName(root.project.competitorName)
						.otherSolutionDescription(root.project.otherSolutionDescription).build();
			}

			// Building the Actual CreateOpportunity Request
			UpdateOpportunityRequest updateOpportunityRequest = UpdateOpportunityRequest.builder().catalog(root.catalog)
					.identifier(root.identifier).lastModifiedDate(Instant.parse(root.lastModifiedDate))
					.primaryNeedsFromAwsWithStrings(root.primaryNeedsFromAws).opportunityType(root.opportunityType)
					.lifeCycle(lifeCycle)
					.customer(customer)
					.project(project)
					.partnerOpportunityIdentifier(root.partnerOpportunityIdentifier)
					.marketing(marketing)
					.nationalSecurity(root.nationalSecurity)
					.opportunityType(root.opportunityType)
					.build();

			UpdateOpportunityResponse updateResponse = client.updateOpportunity(updateOpportunityRequest);
			System.out.println("Successfully updated opportunity: " + updateResponse);

			return updateResponse;
		} else {
			System.out.println("Opportunity cannot be updated.");
			return null;
		}
    }
}
```
+  For API details, see [UpdateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/UpdateOpportunity) in *AWS SDK for Java 2.x API Reference*.

## Scenarios
<a name="scenarios"></a>

### Update associated entity of an opportunity
<a name="partnercentral-selling__UpdateAssociatedEntity_java_topic"></a>

The following code example shows how to:
+ Disassociate an old entity.
+ Associate a new entity.

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Scenarios](https://github.com/aws-samples/partner-crm-integration-samples/tree/main/partner-central-api-sample-codes/java_preview) repository.
Update associated entity of an opportunity

```
package org.example;

import static org.example.utils.Constants.*;

import org.example.utils.Constants;
import org.example.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.partnercentralselling.PartnerCentralSellingClient;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.AssociateOpportunityResponse;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityRequest;
import software.amazon.awssdk.services.partnercentralselling.model.DisassociateOpportunityResponse;

/*
Purpose
PC-API -17 Replacing a solution
*/

public class ReplaceSolution {

	static PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

    public static void main(String[] args) {

    	String opportunityId = args.length > 0 ? args[0] : OPPORTUNITY_ID;

    	String entityType = "Solutions";
    	String originalEntityIdentifier = "S-0000000";
    	String newEntityIdentifier = "S-0011111";

    	disassociateOppornitityResponse(opportunityId, entityType, originalEntityIdentifier );
    	AssociateOpportunityResponse associateOpportunityResponse = associateOpportunityResponse(opportunityId, entityType, newEntityIdentifier );

    	ReferenceCodesUtils.formatOutput(associateOpportunityResponse);
    }

	private static AssociateOpportunityResponse associateOpportunityResponse(String opportunityId, String entityType, String entityIdentifier) {

        AssociateOpportunityRequest associateOpportunityRequest = AssociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();

        AssociateOpportunityResponse response = client.associateOpportunity(associateOpportunityRequest);

        return response;
	}

	private static DisassociateOpportunityResponse disassociateOppornitityResponse(String opportunityId, String entityType, String entityIdentifier) {
		PartnerCentralSellingClient client = PartnerCentralSellingClient.builder()
            .region(Region.US_EAST_1)
            .credentialsProvider(DefaultCredentialsProvider.create())
            .httpClient(ApacheHttpClient.builder().build())
            .build();

        DisassociateOpportunityRequest disassociateOpportunityRequest = DisassociateOpportunityRequest.builder()
				.catalog(Constants.CATALOG_TO_USE)
        		.opportunityIdentifier(opportunityId)
        		.relatedEntityType(entityType)
        		.relatedEntityIdentifier(entityIdentifier)
        		.build();

        DisassociateOpportunityResponse response = client.disassociateOpportunity(disassociateOpportunityRequest);

        return response;
	}
}
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [AssociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AssociateOpportunity)
  + [DisassociateOpportunity](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/DisassociateOpportunity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
