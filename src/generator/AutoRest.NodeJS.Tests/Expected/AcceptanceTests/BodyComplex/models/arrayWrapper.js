/*
 * Copyright (c) Microsoft Corporation. All rights reserved.
 * Licensed under the MIT License. See License.txt in the project root for
 * license information.
 * 
 * Code generated by Microsoft (R) AutoRest Code Generator.
 * Changes may cause incorrect behavior and will be lost if the code is
 * regenerated.
 */

'use strict';

var util = require('util');

/**
 * @class
 * Initializes a new instance of the ArrayWrapper class.
 * @constructor
 * @member {array} [array]
 * 
 */
function ArrayWrapper() {
}

/**
 * Defines the metadata of ArrayWrapper
 *
 * @returns {object} metadata of ArrayWrapper
 *
 */
ArrayWrapper.prototype.mapper = function () {
  return {
    required: false,
    serializedName: 'array-wrapper',
    type: {
      name: 'Composite',
      className: 'ArrayWrapper',
      modelProperties: {
        array: {
          required: false,
          serializedName: 'array',
          type: {
            name: 'Sequence',
            element: {
                required: false,
                serializedName: 'StringElementType',
                type: {
                  name: 'String'
                }
            }
          }
        }
      }
    }
  };
};

module.exports = ArrayWrapper;
