---
source_url: https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/go_redshift_code_examples.html
---

# Amazon Redshift examples using SDK for Go V2
<a name="go_redshift_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon Redshift.

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Basics](#basics)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello Amazon Redshift
<a name="redshift_Hello_go_topic"></a>

The following code example shows how to get started using Amazon Redshift.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
)

// main uses the AWS SDK for Go V2 to create a Redshift client
// and list up to 10 clusters in your account.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {
	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}
	redshiftClient := redshift.NewFromConfig(sdkConfig)
	count := 20
	fmt.Printf("Let's list up to %v clusters for your account.\n", count)
	result, err := redshiftClient.DescribeClusters(ctx, &redshift.DescribeClustersInput{
		MaxRecords: aws.Int32(int32(count)),
	})
	if err != nil {
		fmt.Printf("Couldn't list clusters for your account. Here's why: %v\n", err)
		return
	}
	if len(result.Clusters) == 0 {
		fmt.Println("You don't have any clusters!")
		return
	}
	for _, cluster := range result.Clusters {
		fmt.Printf("\t%v : %v\n", *cluster.ClusterIdentifier, *cluster.ClusterStatus)
	}
}
```
+  For API details, see [DescribeClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeClusters) in *AWS SDK for Go API Reference*.

## Basics
<a name="basics"></a>

### Learn the basics
<a name="redshift_Scenario_go_topic"></a>

The following code example shows how to:
+ Create a Redshift cluster.
+ List databases in the cluster.
+ Create a table named Movies.
+ Populate the Movies table.
+ Query the Movies table by year.
+ Modify the Redshift cluster.
+ Delete the Amazon Redshift cluster.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
package scenarios

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"math/rand"
	"strings"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	redshift_types "github.com/aws/aws-sdk-go-v2/service/redshift/types"
	redshiftdata_types "github.com/aws/aws-sdk-go-v2/service/redshiftdata/types"
	"github.com/aws/aws-sdk-go-v2/service/secretsmanager"
	"github.com/awsdocs/aws-doc-sdk-examples/gov2/demotools"
	"github.com/awsdocs/aws-doc-sdk-examples/gov2/redshift/actions"

	"github.com/aws/aws-sdk-go-v2/service/redshift"
	"github.com/aws/aws-sdk-go-v2/service/redshiftdata"
)

// IScenarioHelper abstracts input and wait functions from a scenario so that they
// can be mocked for unit testing.
type IScenarioHelper interface {
	GetName() string
}

const rMax = 100000

type ScenarioHelper struct {
	Prefix string
	Random *rand.Rand
}

// GetName returns a unique name formed of a prefix and a random number.
func (helper ScenarioHelper) GetName() string {
	return fmt.Sprintf("%v%v", helper.Prefix, helper.Random.Intn(rMax))
}

// RedshiftBasicsScenario separates the steps of this scenario into individual functions so that
// they are simpler to read and understand.
type RedshiftBasicsScenario struct {
	sdkConfig         aws.Config
	helper            IScenarioHelper
	questioner        demotools.IQuestioner
	pauser            demotools.IPausable
	filesystem        demotools.IFileSystem
	redshiftActor     *actions.RedshiftActions
	redshiftDataActor *actions.RedshiftDataActions
	secretsmanager    *SecretsManager
}

// SecretsManager is used to retrieve username and password information from a secure service.
type SecretsManager struct {
	SecretsManagerClient *secretsmanager.Client
}

// RedshiftBasics constructs a new Redshift Basics runner.
func RedshiftBasics(sdkConfig aws.Config, questioner demotools.IQuestioner, pauser demotools.IPausable, filesystem demotools.IFileSystem, helper IScenarioHelper) RedshiftBasicsScenario {
	scenario := RedshiftBasicsScenario{
		sdkConfig:         sdkConfig,
		helper:            helper,
		questioner:        questioner,
		pauser:            pauser,
		filesystem:        filesystem,
		secretsmanager:    &SecretsManager{SecretsManagerClient: secretsmanager.NewFromConfig(sdkConfig)},
		redshiftActor:     &actions.RedshiftActions{RedshiftClient: redshift.NewFromConfig(sdkConfig)},
		redshiftDataActor: &actions.RedshiftDataActions{RedshiftDataClient: redshiftdata.NewFromConfig(sdkConfig)},
	}
	return scenario
}

// Movie makes it easier to use Movie objects given in json format.
type Movie struct {
	ID    int    `json:"id"`
	Title string `json:"title"`
	Year  int    `json:"year"`
}

// User makes it easier to get the User data back from SecretsManager and use it later.
type User struct {
	Username string `json:"userName"`
	Password string `json:"userPassword"`
}

// Run runs the RedshiftBasics interactive example that shows you how to use Amazon
// Redshift and how to interact with its common endpoints.
//
// 0. Retrieve username and password information to access Redshift.
// 1. Create a cluster.
// 2. Wait for the cluster to become available.
// 3. List the available databases in the region.
// 4. Create a table named "Movies" in the "dev" database.
// 5. Populate the movies table from the "movies.json" file.
// 6. Query the movies table by year.
// 7. Modify the cluster's maintenance window.
// 8. Optionally clean up all resources created during this demo.
//
// This example creates an Amazon Redshift service client from the specified sdkConfig so that
// you can replace it with a mocked or stubbed config for unit testing.
//
// It uses a questioner from the `demotools` package to get input during the example.
// This package can be found in the ..\..\demotools folder of this repo.
func (runner *RedshiftBasicsScenario) Run(ctx context.Context) {

	user := User{}
	secretId := "s3express/basics/secrets"
	clusterId := "demo-cluster-1"
	maintenanceWindow := "wed:07:30-wed:08:00"
	databaseName := "dev"
	tableName := "Movies"
	fileName := "Movies.json"
	nodeType := "ra3.xlplus"
	clusterType := "single-node"

	defer func() {
		if r := recover(); r != nil {
			log.Println("Something went wrong with the demo.")
			_, isMock := runner.questioner.(*demotools.MockQuestioner)
			if isMock || runner.questioner.AskBool("Do you want to see the full error message (y/n)?", "y") {
				log.Println(r)
			}
			runner.cleanUpResources(ctx, clusterId, databaseName, tableName, user.Username, runner.questioner)
		}
	}()

	// Retrieve the userName and userPassword from SecretsManager
	output, err := runner.secretsmanager.SecretsManagerClient.GetSecretValue(ctx, &secretsmanager.GetSecretValueInput{
		SecretId: aws.String(secretId),
	})
	if err != nil {
		log.Printf("There was a problem getting the secret value: %s", err)
		log.Printf("Please make sure to create a secret named 's3express/basics/secrets' with keys of 'userName' and 'userPassword'.")
		panic(err)
	}

	err = json.Unmarshal([]byte(*output.SecretString), &user)
	if err != nil {
		log.Printf("There was a problem parsing the secret value from JSON: %s", err)
		panic(err)
	}

	// Create the Redshift cluster
	_, err = runner.redshiftActor.CreateCluster(ctx, clusterId, user.Username, user.Password, nodeType, clusterType, true)
	if err != nil {
		var clusterAlreadyExistsFault *redshift_types.ClusterAlreadyExistsFault
		if errors.As(err, &clusterAlreadyExistsFault) {
			log.Println("Cluster already exists. Continuing.")
		} else {
			log.Println("Error creating cluster.")
			panic(err)
		}
	}

	// Wait for the cluster to become available
	waiter := redshift.NewClusterAvailableWaiter(runner.redshiftActor.RedshiftClient)
	err = waiter.Wait(ctx, &redshift.DescribeClustersInput{
		ClusterIdentifier: aws.String(clusterId),
	}, 5*time.Minute)
	if err != nil {
		log.Println("An error occurred waiting for the cluster.")
		panic(err)
	}

	// Get some info about the cluster
	describeOutput, err := runner.redshiftActor.DescribeClusters(ctx, clusterId)
	if err != nil {
		log.Println("Something went wrong trying to get information about the cluster.")
		panic(err)
	}
	log.Println("Here's some information about the cluster.")
	log.Printf("The cluster's status is %s", *describeOutput.Clusters[0].ClusterStatus)
	log.Printf("The cluster was created at %s", *describeOutput.Clusters[0].ClusterCreateTime)

	// List databases
	log.Println("List databases in", clusterId)
	runner.questioner.Ask("Press Enter to continue...")
	err = runner.redshiftDataActor.ListDatabases(ctx, clusterId, databaseName, user.Username)
	if err != nil {
		log.Printf("Failed to list databases: %v\n", err)
		panic(err)
	}

	// Create the "Movies" table
	log.Println("Now you will create a table named " + tableName + ".")
	runner.questioner.Ask("Press Enter to continue...")
	err = nil
	result, err := runner.redshiftDataActor.CreateTable(ctx, clusterId, databaseName, tableName, user.Username, runner.pauser, []string{"title VARCHAR(256)", "year INT"})
	if err != nil {
		log.Printf("Failed to create table: %v\n", err)
		panic(err)
	}

	describeInput := redshiftdata.DescribeStatementInput{
		Id: result.Id,
	}
	query := actions.RedshiftQuery{
		Context: ctx,
		Input:   describeInput,
		Result:  result,
	}
	err = runner.redshiftDataActor.WaitForQueryStatus(query, runner.pauser, true)
	if err != nil {
		log.Printf("Failed to execute query: %v\n", err)
		panic(err)
	}
	log.Printf("Successfully executed query\n")

	// Populate the "Movies" table
	runner.PopulateMoviesTable(ctx, clusterId, databaseName, tableName, user.Username, fileName)

	// Query the "Movies" table by year
	log.Println("Query the Movies table by year.")
	year := runner.questioner.AskInt(
		fmt.Sprintf("Enter a value between %v and %v:", 2012, 2014),
		demotools.InIntRange{Lower: 2012, Upper: 2014})
	runner.QueryMoviesByYear(ctx, clusterId, databaseName, tableName, user.Username, year)

	// Modify the cluster's maintenance window
	runner.redshiftActor.ModifyCluster(ctx, clusterId, maintenanceWindow)

	// Delete the Redshift cluster if confirmed
	runner.cleanUpResources(ctx, clusterId, databaseName, tableName, user.Username, runner.questioner)

	log.Println("Thanks for watching!")
}

// cleanUpResources asks the user if they would like to delete each resource created during the scenario, from most
// impactful to least impactful. If any choice to delete is made, further deletion attempts are skipped.
func (runner *RedshiftBasicsScenario) cleanUpResources(ctx context.Context, clusterId string, databaseName string, tableName string, userName string, questioner demotools.IQuestioner) {
	deleted := false
	var err error = nil
	if questioner.AskBool("Do you want to delete the entire cluster? This will clean up all resources. (y/n)", "y") {
		deleted, err = runner.redshiftActor.DeleteCluster(ctx, clusterId)
		if err != nil {
			log.Printf("Error deleting cluster: %v", err)
		}
	}
	if !deleted && questioner.AskBool("Do you want to delete the dev table? This will clean up all inserted records but keep your cluster intact. (y/n)", "y") {
		deleted, err = runner.redshiftDataActor.DeleteTable(ctx, clusterId, databaseName, tableName, userName)
		if err != nil {
			log.Printf("Error deleting movies table: %v", err)
		}
	}
	if !deleted && questioner.AskBool("Do you want to delete all rows in the Movies table? This will clean up all inserted records but keep your cluster and table intact. (y/n)", "y") {
		deleted, err = runner.redshiftDataActor.DeleteDataRows(ctx, clusterId, databaseName, tableName, userName, runner.pauser)
		if err != nil {
			log.Printf("Error deleting data rows: %v", err)
		}
	}
	if !deleted {
		log.Print("Please manually delete any unwanted resources.")
	}
}

// loadMoviesFromJSON takes the <fileName> file and populates a slice of Movie objects.
func (runner *RedshiftBasicsScenario) loadMoviesFromJSON(fileName string, filesystem demotools.IFileSystem) ([]Movie, error) {
	file, err := filesystem.OpenFile("../../resources/sample_files/" + fileName)
	if err != nil {
		return nil, err
	}
	defer filesystem.CloseFile(file)

	var movies []Movie
	err = json.NewDecoder(file).Decode(&movies)
	if err != nil {
		return nil, err
	}

	return movies, nil
}

// PopulateMoviesTable reads data from the <fileName> file and inserts records into the "Movies" table.
func (runner *RedshiftBasicsScenario) PopulateMoviesTable(ctx context.Context, clusterId string, databaseName string, tableName string, userName string, fileName string) {
	log.Println("Populate the " + tableName + " table using the " + fileName + " file.")
	numRecords := runner.questioner.AskInt(
		fmt.Sprintf("Enter a value between %v and %v:", 10, 100),
		demotools.InIntRange{Lower: 10, Upper: 100})

	movies, err := runner.loadMoviesFromJSON(fileName, runner.filesystem)
	if err != nil {
		log.Printf("Failed to load movies from JSON: %v\n", err)
		panic(err)
	}

	var sqlStatements []string

	for i, movie := range movies {
		if i >= numRecords {
			break
		}

		sqlStatement := fmt.Sprintf(`INSERT INTO %s (title, year) VALUES ('%s', %d);`,
			tableName,
			strings.Replace(movie.Title, "'", "''", -1), // Double any single quotes to escape them
			movie.Year)

		sqlStatements = append(sqlStatements, sqlStatement)
	}

	input := &redshiftdata.BatchExecuteStatementInput{
		ClusterIdentifier: aws.String(clusterId),
		Database:          aws.String(databaseName),
		DbUser:            aws.String(userName),
		Sqls:              sqlStatements,
	}

	result, err := runner.redshiftDataActor.ExecuteBatchStatement(ctx, *input)
	if err != nil {
		log.Printf("Failed to execute batch statement: %v\n", err)
		panic(err)
	}

	describeInput := redshiftdata.DescribeStatementInput{
		Id: result.Id,
	}

	query := actions.RedshiftQuery{
		Context: ctx,
		Result:  result,
		Input:   describeInput,
	}
	err = runner.redshiftDataActor.WaitForQueryStatus(query, runner.pauser, true)
	if err != nil {
		log.Printf("Failed to execute batch insert query: %v\n", err)
		return
	}
	log.Printf("Successfully executed batch statement\n")

	log.Printf("%d records were added to the Movies table.\n", numRecords)
}

// QueryMoviesByYear retrieves only movies from the "Movies" table which match the given year.
func (runner *RedshiftBasicsScenario) QueryMoviesByYear(ctx context.Context, clusterId string, databaseName string, tableName string, userName string, year int) {

	sqlStatement := fmt.Sprintf(`SELECT title FROM %s WHERE year = %d;`, tableName, year)

	input := &redshiftdata.ExecuteStatementInput{
		ClusterIdentifier: aws.String(clusterId),
		Database:          aws.String(databaseName),
		DbUser:            aws.String(userName),
		Sql:               aws.String(sqlStatement),
	}

	result, err := runner.redshiftDataActor.ExecuteStatement(ctx, *input)
	if err != nil {
		log.Printf("Failed to query movies: %v\n", err)
		panic(err)
	}

	log.Println("The identifier of the statement is ", *result.Id)

	describeInput := redshiftdata.DescribeStatementInput{
		Id: result.Id,
	}

	query := actions.RedshiftQuery{
		Context: ctx,
		Input:   describeInput,
		Result:  result,
	}
	err = runner.redshiftDataActor.WaitForQueryStatus(query, runner.pauser, true)
	if err != nil {
		log.Printf("Failed to execute query: %v\n", err)
		panic(err)
	}
	log.Printf("Successfully executed query\n")

	getResultOutput, err := runner.redshiftDataActor.GetStatementResult(ctx, *result.Id)
	if err != nil {
		log.Printf("Failed to query movies: %v\n", err)
		panic(err)
	}
	for _, row := range getResultOutput.Records {
		for _, col := range row {
			title, ok := col.(*redshiftdata_types.FieldMemberStringValue)
			if !ok {
				log.Println("Failed to parse the field")
			} else {
				log.Printf("The Movie title field is %s\n", title.Value)
			}
		}
	}
}
```
+ For API details, see the following topics in *AWS SDK for Go API Reference*.
  + [CreateCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.CreateCluster)
  + [DescribeClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeClusters)
  + [DescribeStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeStatement)
  + [ExecuteStatement](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.ExecuteStatement)
  + [GetStatementResult](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.GetStatementResult)
  + [ListDatabasesPaginator](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.ListDatabasesPaginator)
  + [ModifyCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.ModifyCluster)

## Actions
<a name="actions"></a>

### `CreateCluster`
<a name="redshift_CreateCluster_go_topic"></a>

The following code example shows how to use `CreateCluster`.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
import (
	"context"
	"errors"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
	"github.com/aws/aws-sdk-go-v2/service/redshift/types"
)

// RedshiftActions wraps Redshift service actions.
type RedshiftActions struct {
	RedshiftClient *redshift.Client
}

// CreateCluster sends a request to create a cluster with the given clusterId using the provided credentials.
func (actor RedshiftActions) CreateCluster(ctx context.Context, clusterId string, userName string, userPassword string, nodeType string, clusterType string, publiclyAccessible bool) (*redshift.CreateClusterOutput, error) {
	// Create a new Redshift cluster
	input := &redshift.CreateClusterInput{
		ClusterIdentifier:  aws.String(clusterId),
		MasterUserPassword: aws.String(userPassword),
		MasterUsername:     aws.String(userName),
		NodeType:           aws.String(nodeType),
		ClusterType:        aws.String(clusterType),
		PubliclyAccessible: aws.Bool(publiclyAccessible),
	}
	var opErr *types.ClusterAlreadyExistsFault
	output, err := actor.RedshiftClient.CreateCluster(ctx, input)
	if err != nil && errors.As(err, &opErr) {
		log.Println("Cluster already exists")
		return nil, nil
	} else if err != nil {
		log.Printf("Failed to create Redshift cluster: %v\n", err)
		return nil, err
	}

	log.Printf("Created cluster %s\n", *output.Cluster.ClusterIdentifier)
	return output, nil
}
```
+  For API details, see [CreateCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.CreateCluster) in *AWS SDK for Go API Reference*.

### `DeleteCluster`
<a name="redshift_DeleteCluster_go_topic"></a>

The following code example shows how to use `DeleteCluster`.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
import (
	"context"
	"errors"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
	"github.com/aws/aws-sdk-go-v2/service/redshift/types"
)

// RedshiftActions wraps Redshift service actions.
type RedshiftActions struct {
	RedshiftClient *redshift.Client
}

// DeleteCluster deletes the given cluster.
func (actor RedshiftActions) DeleteCluster(ctx context.Context, clusterId string) (bool, error) {
	input := redshift.DeleteClusterInput{
		ClusterIdentifier:        aws.String(clusterId),
		SkipFinalClusterSnapshot: aws.Bool(true),
	}
	_, err := actor.RedshiftClient.DeleteCluster(ctx, &input)
	var opErr *types.ClusterNotFoundFault
	if err != nil && errors.As(err, &opErr) {
		log.Println("Cluster was not found. Where could it be?")
		return false, err
	} else if err != nil {
		log.Printf("Failed to delete Redshift cluster: %v\n", err)
		return false, err
	}
	waiter := redshift.NewClusterDeletedWaiter(actor.RedshiftClient)
	err = waiter.Wait(ctx, &redshift.DescribeClustersInput{
		ClusterIdentifier: aws.String(clusterId),
	}, 5*time.Minute)
	if err != nil {
		log.Printf("Wait time exceeded for deleting cluster, continuing: %v\n", err)
	}
	log.Printf("The cluster %s was deleted\n", clusterId)
	return true, nil
}
```
+  For API details, see [DeleteCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DeleteCluster) in *AWS SDK for Go API Reference*.

### `DescribeClusters`
<a name="redshift_DescribeClusters_go_topic"></a>

The following code example shows how to use `DescribeClusters`.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
import (
	"context"
	"errors"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
	"github.com/aws/aws-sdk-go-v2/service/redshift/types"
)

// RedshiftActions wraps Redshift service actions.
type RedshiftActions struct {
	RedshiftClient *redshift.Client
}

// DescribeClusters returns information about the given cluster.
func (actor RedshiftActions) DescribeClusters(ctx context.Context, clusterId string) (*redshift.DescribeClustersOutput, error) {
	input, err := actor.RedshiftClient.DescribeClusters(ctx, &redshift.DescribeClustersInput{
		ClusterIdentifier: aws.String(clusterId),
	})
	var opErr *types.AccessToClusterDeniedFault
	if errors.As(err, &opErr) {
		println("Access to cluster denied.")
		panic(err)
	} else if err != nil {
		println("Failed to describe Redshift clusters.")
		return nil, err
	}
	return input, nil
}
```
+  For API details, see [DescribeClusters](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.DescribeClusters) in *AWS SDK for Go API Reference*.

### `ModifyCluster`
<a name="redshift_ModifyCluster_go_topic"></a>

The following code example shows how to use `ModifyCluster`.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/redshift#code-examples).

```
import (
	"context"
	"errors"
	"log"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/redshift"
	"github.com/aws/aws-sdk-go-v2/service/redshift/types"
)

// RedshiftActions wraps Redshift service actions.
type RedshiftActions struct {
	RedshiftClient *redshift.Client
}

// ModifyCluster sets the preferred maintenance window for the given cluster.
func (actor RedshiftActions) ModifyCluster(ctx context.Context, clusterId string, maintenanceWindow string) *redshift.ModifyClusterOutput {
	// Modify the cluster's maintenance window
	input := &redshift.ModifyClusterInput{
		ClusterIdentifier:          aws.String(clusterId),
		PreferredMaintenanceWindow: aws.String(maintenanceWindow),
	}

	var opErr *types.InvalidClusterStateFault
	output, err := actor.RedshiftClient.ModifyCluster(ctx, input)
	if err != nil && errors.As(err, &opErr) {
		log.Println("Cluster is in an invalid state.")
		panic(err)
	} else if err != nil {
		log.Printf("Failed to modify Redshift cluster: %v\n", err)
		panic(err)
	}

	log.Printf("The cluster was successfully modified and now has %s as the maintenance window\n", *output.Cluster.PreferredMaintenanceWindow)
	return output
}
```
+  For API details, see [ModifyCluster](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/redshift#Client.ModifyCluster) in *AWS SDK for Go API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Go v2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-go` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
