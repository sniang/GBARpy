more doc_class/README.md > README.md

classname=('BeamSpot' 'FitInterface' 'SimpleGaussian' 'FilteredGaussian' 'TwoGaussians' 'MCPParams')
for name in "${classname[@]}"
do
    md_name="doc_class/${name}.md"
    myopts src/GBARpy/MCPPicture.py -o $md_name -c $name -s false -t "GBARpy.MCPPicture.${name}"
    
    sed "s/Returns/* Returns/g" $md_name > doc_class/temp.md
    sed "/---/d" doc_class/temp.md > $md_name
    sed "s/Examples/* Examples/g" $md_name > doc_class/temp.md
    sed "s/   \`\`\`python/\`\`\`python/g" doc_class/temp.md > $md_name
    echo "\n" >>  $md_name
    rm doc_class/temp.md
    more $md_name >> README.md
done
