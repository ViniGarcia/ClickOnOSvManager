//VNF_HEADER
//VNF_VERSION: 1.0
//VNF_ID:979eaf94-ad8c-4aef-90fa-c29189b42fde
//VNF_PROVIDER:UFSM
//VNF_NAME:Print
//VNF_RELEASE_DATE:2017-04-08 21-45-45
//VNF_RELEASE_VERSION:1.0
//VNF_RELEASE_LIFESPAN:2017-06-08 21-45
//VNF_DESCRIPTION: Print received packets
FromDPDKDevice(0) -> Print() -> Discard;