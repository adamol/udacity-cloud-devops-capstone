eksctl create cluster \
	--name $1 \
	--node-type t2.small \
	--nodes 2 \
	--nodes-min 1 \
	--nodes-max 3 \
	--managed

