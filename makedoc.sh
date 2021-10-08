more doc_class/README.md > README.md

classname=('BeamSpot' 'FitInterface' 'SimpleGaussian' 'FilteredGaussian' 'TwoGaussians' 'MCPParams' 'Others')
for name in "${classname[@]}"
do
    md_name="doc_class/${name}.md"
    if [ $name = 'Others' ]
    then
    myopts src/GBARpy/MCPPicture.py -o $md_name -t "Other functions"
    else
    myopts src/GBARpy/MCPPicture.py -o $md_name -c $name -s false -t "GBARpy.MCPPicture.${name}"
    fi
    
    sed "s/Returns/* Returns/g" $md_name > doc_class/temp.md
    sed "/---/d" doc_class/temp.md > $md_name
    sed "s/Examples/* Examples/g" $md_name > doc_class/temp.md
    sed "s/   \`\`\`python/\`\`\`python/g" doc_class/temp.md > $md_name
    echo "\n" >>  $md_name
    rm doc_class/temp.md
    more $md_name >> README.md
done

table="# GBARpy\n## Table of contents\n"
input="README.md"
hash1='^\# '
pt1='* ['
hash2="^\## "
pt2='\t* ['

while IFS= read -r line
do
    link="${line/'# '/}"
    link="${link/'#'/}"
    link="${link// /-}"
    if [[ $line =~ $hash1 ]]
    then
        res="${line/'# '/$pt1}"
        table+="${res}](#${link})\n"
    fi
    if [[ $line =~ $hash2 ]]
    then
        res="${line/'## '/$pt2}"
        table+="${res}](#${link})\n"
    fi
done < "$input"

echo "$table$(cat README.md)" > README.md

