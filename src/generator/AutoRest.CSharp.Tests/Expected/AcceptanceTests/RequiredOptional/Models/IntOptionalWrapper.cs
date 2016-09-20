// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License. See License.txt in the project root for
// license information.
// 
// Code generated by Microsoft (R) AutoRest Code Generator.
// Changes may cause incorrect behavior and will be lost if the code is
// regenerated.

namespace Fixtures.AcceptanceTestsRequiredOptional.Models
{
    using System.Linq;

    public partial class IntOptionalWrapper
    {
        /// <summary>
        /// Initializes a new instance of the IntOptionalWrapper class.
        /// </summary>
        public IntOptionalWrapper() { }

        /// <summary>
        /// Initializes a new instance of the IntOptionalWrapper class.
        /// </summary>
        public IntOptionalWrapper(int? value = default(int?))
        {
            Value = value;
        }

        /// <summary>
        /// </summary>
        [Newtonsoft.Json.JsonProperty(PropertyName = "value")]
        public int? Value { get; set; }

    }
}
