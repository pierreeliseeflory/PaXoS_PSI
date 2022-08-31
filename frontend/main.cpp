#include <iostream>

#include "ProtocolParty.h"
#include <chrono>

#include <cryptoTools/Common/Matrix.h>

#include <cryptoTools/Common/Defines.h>
using namespace osuCrypto;

#include "libOTe/TwoChooseOne/KosOtExtReceiver.h"
#include "libOTe/TwoChooseOne/KosOtExtSender.h"
#include "libOTe/TwoChooseOne/KosDotExtReceiver.h"
#include "libOTe/TwoChooseOne/KosDotExtSender.h"

#include <cryptoTools/Network/Channel.h>
#include <cryptoTools/Network/Endpoint.h>
#include <cryptoTools/Network/IOService.h>
#include <numeric>
#include <cryptoTools/Common/Timer.h>
#include <cryptoTools/Common/Log.h>

#include "libOTe/Tools/LinearCode.h"
#include "libOTe/Tools/bch511.h"
#include "libOTe/NChooseOne/Oos/OosNcoOtReceiver.h"
#include "libOTe/NChooseOne/Oos/OosNcoOtSender.h"
#include "libOTe/NChooseOne/Kkrt/KkrtNcoOtReceiver.h"
#include "libOTe/NChooseOne/Kkrt/KkrtNcoOtSender.h"

#include "libOTe/TwoChooseOne/IknpOtExtReceiver.h"
#include "libOTe/TwoChooseOne/IknpOtExtSender.h"

#include "libOTe/NChooseK/AknOtReceiver.h"
#include "libOTe/NChooseK/AknOtSender.h"
#include "libOTe/TwoChooseOne/LzKosOtExtReceiver.h"
#include "libOTe/TwoChooseOne/LzKosOtExtSender.h"

#include "main.h"

#include "libOTe/TwoChooseOne/OTExtInterface.h"

#include "libOTe/Tools/Tools.h"
#include "libOTe/Tools/LinearCode.h"
#include <cryptoTools/Network/Channel.h>
#include <cryptoTools/Network/Endpoint.h>
#include <cryptoTools/Network/IOService.h>
#include <cryptoTools/Common/Log.h>
#include "PsiDefines.h"

#include <thread>
#include <vector>
#include <stdarg.h>

// Usage : ./bin/frontend.exe -partyID 0 -hashSize 1000000 -fieldSize 132 -partiesFile bin/Parties.txt -reportStatistics 0 -internalIterationsNumber 1

int main(int argc, char **argv)
{
    CmdParser parser;
    std::cout << std::endl
              << "=> Parsing arguments" << std::endl
              << std::endl;
    auto parameters = parser.parseArguments("", argc, argv);
    int partyID = stoi(parser.getValueByKey(parameters, "partyID"));

    if (partyID == 0)
    {
        std::cout << std::endl
                  << "=> Initialization" << std::endl
                  << std::endl;
        Receiver receiver(argc, argv);
        std::cout << std::endl
                  << "=> Running PSI" << std::endl
                  << std::endl;
        receiver.run();
    }
    else
    {
        std::cout << std::endl
                  << "=> Initialization" << std::endl
                  << std::endl;
        Sender sender(argc, argv);
        std::cout << std::endl
                  << "=> Running PSI" << std::endl
                  << std::endl;
        sender.run();
    }
}