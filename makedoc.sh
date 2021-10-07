mkdir doc_class
myopts src/GBARpy/MCPPicture.py -o doc_class/BeamSpot.md -c BeamSpot

myopts src/GBARpy/MCPPicture.py -o doc_class/MCPParams.md -c MCPParams -s false -t "GBARpy.MCPPicture.MCPParams"

sed "s/Returns/* Returns/g" doc_class/MCPParams.md > doc_class/temp.md
sed "/---/d" doc_class/temp.md > doc_class/MCPParams.md
sed "s/Examples/*Examples/g" doc_class/MCPParams.md > doc_class/temp.md
cat doc_class/temp.md > doc_class/MCPParams.md

rm doc_class/temp.md

