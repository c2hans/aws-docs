---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_partnercentral-selling_code_examples.html
---

# Partner Central examples using SDK for Go V2
<a name="go_partnercentral-selling_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Partner Central.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `GetOpportunity`
<a name="partnercentral-selling_GetOpportunity_go_topic"></a>

The following code example shows how to use `GetOpportunity`.

**SDK for Go V2**
Get an opportunity.

```
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/partnercentralselling"
)

func main() {
	config, err := config.LoadDefaultConfig(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	config.Region = "us-east-1"

	client := partnercentralselling.NewFromConfig(config)

	output, err := client.GetOpportunity(context.TODO(), &partnercentralselling.GetOpportunityInput{
		Identifier: aws.String("O1111111"),
		Catalog:    aws.String("AWS"),
	})

	if err != nil {
		log.Fatal(err)
	}
	log.Println("printing opportuniy...\n")

	jsonOutput, err := json.MarshalIndent(output, "", "    ")

	fmt.Println(string(jsonOutput))
}
```
+  For API details, see [GetOpportunity](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.GetOpportunity) in *AWS SDK for Go API Reference*.

### `ListOpportunities`
<a name="partnercentral-selling_ListOpportunities_go_topic"></a>

The following code example shows how to use `ListOpportunities`.

**SDK for Go V2**
List opportunities.

```
package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/partnercentralselling"
)

func main() {
	config, err := config.LoadDefaultConfig(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	config.Region = "us-east-1"

	client := partnercentralselling.NewFromConfig(config)

	output, err := client.ListOpportunities(context.TODO(), &partnercentralselling.ListOpportunitiesInput{
		MaxResults: aws.Int32(2),
		Catalog:    aws.String("AWS"),
	})

	if err != nil {
		log.Fatal(err)
	}

	jsonOutput, err := json.MarshalIndent(output, "", "    ")
	fmt.Println(string(jsonOutput))
}
```
+  For API details, see [ListOpportunities](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/partnercentralselling#Client.ListOpportunities) in *AWS SDK for Go API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
