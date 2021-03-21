aws cloudformation delete-stack --stack-name prod-brownbag
./upsert_stack.sh prod-brownbag prod/db.yml --capabilities CAPABILITY_AUTO_EXPAND
