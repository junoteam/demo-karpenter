## # Makefile help
##
## make        # Prints this help message
## make help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

##
## # Doc Generation
##

## make tf-docs    # Generate terraform module documentation 
tf-docs:
	$(MAKE) -C terraform docs

ENVIRONMENT ?= dev
PARALLELISM ?= 80
TARGET ?=
##
## # Terragrunt helpers
##
## export ENVIRONMENT=prod  # prod is the default environment
##
## make init   	          # Run a terragrunt init
$(info WORKING ENVIRONMENT="$(ENVIRONMENT)")
init:
	cd terraform/live/$(ENVIRONMENT)/ && \
		terragrunt init

## make plan                # Run a terragrunt plan
## make apply               # Run a terragrunt apply
## make apply-auto-approve  # Run a terragrunt auto apply
plan:
	cd terraform/environments/$(ENVIRONMENT)/ && \
		terragrunt plan --parallelism $(PARALLELISM)

apply:
	cd terraform/environments/$(ENVIRONMENT)/ && \
		terragrunt apply --parallelism $(PARALLELISM)

apply-auto-approve:
	cd terraform/environments/$(ENVIRONMENT)/ && \
		terragrunt apply -auto-approve --parallelism $(PARALLELISM)

destroy-resource:
	cd terraform/environments/$(ENVIRONMENT)/ && \
		terragrunt destroy -target=$(TARGET)
