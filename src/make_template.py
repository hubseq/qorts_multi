import json
MODULE = 'qorts_multi'

mi_template_json = {'module_version': '00.00.00', 'program_name': 'qorts', 'program_subname': '', 'program_version': '3.8', 'compute': {'environment': 'aws', 'language': 'R', 'language_version': '4.1', 'vcpus': 2, 'memory': 6000}, 'program_arguments': '', 'program_input': [{'input_type': 'folder', 'input_file_type': '', 'input_position': 0, 'input_prefix': ''}], 'program_output': [{'output_type': 'folder', 'output_file_type': '', 'output_position': -1, 'output_prefix': ''}], 'alternate_inputs': [], 'alternate_outputs': [], 'defaults': {}}
with open(MODULE+'.template.json','w') as fout:
    json.dump(mi_template_json, fout)

io_dryrun_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/qorts/'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts_multi/'],  'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '-samples rnastar_test_tiny1,rnastar_test_tiny2,rnastar_test_tiny3,rnastar_test_tiny4,rnastar_test_tiny5,rnastar_test_tiny6 -lanes rep1,rep2,rep3,rep1,rep2,rep3 -groups control,control,control,drug,drug,drug', 'sample_id': 'qorts_multi_test', 'dryrun': ''}
io_json = {'input': ['s3://hubtenants/test/rnaseq/run_test1/qorts/'], 'output': ['s3://hubtenants/test/rnaseq/run_test1/qorts_multi/'],  'alternate_inputs': [], 'alternate_outputs': [], 'program_arguments': '-samples rnastar_test_tiny1,rnastar_test_tiny2,rnastar_test_tiny3,rnastar_test_tiny4,rnastar_test_tiny5,rnastar_test_tiny6 -lanes rep1,rep2,rep3,rep1,rep2,rep3 -groups control,control,control,drug,drug,drug', 'sample_id': 'qorts_multi_test'}


with open(MODULE+'.dryrun_test.io.json','w') as fout:
    json.dump(io_dryrun_json, fout)
with open(MODULE+'.test.io.json','w') as fout:
    json.dump(io_json, fout)
    
# job info test JSONs                                                                                                        
job_json = {"container_overrides": {"command": ["--module_name", MODULE, "--run_arguments", "s3://hubseq-data/modules/"+MODULE+"/job/"+MODULE+".test.io.json", "--working_dir", "/home/"]}, "jobqueue": "batch_scratch_queue", "jobname": "job_"+MODULE+"_test"}
with open(MODULE+'.test.job.json','w') as fout:
    json.dump(job_json, fout)

    
