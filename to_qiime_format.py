import pandas as pd 

manifest_path = 'manifests/hmp_local_pt_female.tsv'
df = pd.read_csv(manifest_path, sep='\t')

qiime_manifest = df[['sample_id', 'urls']].rename(columns = {'sample_id':'sample-id', 'urls':'absolute-filepath'})

export_path = 'manifests/for_qiime/qiime_pt_f.tsv'
qiime_manifest.to_csv(export_path,sep='\t', index=False)

print(f"QIIME-compatible manifest saved to: {export_path}")
