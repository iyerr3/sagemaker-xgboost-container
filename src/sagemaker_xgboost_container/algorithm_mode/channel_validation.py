# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from sagemaker_algorithm_toolkit import channel_validation as cv


def initialize():
    train_channel = cv.Channel(name="train", required=True)
    train_channel.add("csv", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    train_channel.add("csv", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    train_channel.add("libsvm", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    train_channel.add("libsvm", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    train_channel.add("text/csv", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    train_channel.add("text/csv", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    train_channel.add("text/libsvm", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    train_channel.add("text/libsvm", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)

    validation_channel = cv.Channel(name="validation", required=False)
    validation_channel.add("csv", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    validation_channel.add("csv", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    validation_channel.add("libsvm", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    validation_channel.add("libsvm", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    validation_channel.add("text/csv", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    validation_channel.add("text/csv", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)
    validation_channel.add("text/libsvm", cv.Channel.FILE_MODE, cv.Channel.SHARDED)
    validation_channel.add("text/libsvm", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)

    # new for script mode/algorithm mode toggle
    code_channel = cv.Channel(name="code", required=False)
    code_channel.add("text/python", cv.Channel.FILE_MODE, cv.Channel.REPLICATED)

    return cv.Channels(train_channel, validation_channel, code_channel)
