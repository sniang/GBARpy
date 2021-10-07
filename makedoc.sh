mkdir doc_class
myopts src/GBARpy/MCPPicture.py -o doc_class/BeamSpot.md -c BeamSpot -s false -t "GBARpy.MCPPicture.BeamSpot"

myopts src/GBARpy/MCPPicture.py -o doc_class/MCPParams.md -c MCPParams -s false -t "GBARpy.MCPPicture.MCPParams"

sed "s/Returns/* Returns/g" doc_class/BeamSpot.md > doc_class/temp.md
sed "/---/d" doc_class/temp.md > doc_class/BeamSpot.md
sed "s/Examples/* Examples/g" doc_class/BeamSpot.md > doc_class/temp.md
sed "s/   ```python/python/g" doc_class/temp.md > doc_class/BeamSpot.md
echo "\n" >>  doc_class/BeamSpot.md
rm doc_class/temp.md

sed "s/Returns/* Returns/g" doc_class/MCPParams.md > doc_class/temp.md
sed "/---/d" doc_class/temp.md > doc_class/MCPParams.md
sed "s/Examples/* Examples/g" doc_class/MCPParams.md > doc_class/temp.md
sed "s/   ```python/python/g" doc_class/temp.md > doc_class/MCPParams.md
echo "\n" >> doc_class/MCPParams.md
rm doc_class/temp.md

more doc_class/README.md > README.md
more doc_class/BeamSpot.md >> README.md
more doc_class/MCPParams.md >> README.md

